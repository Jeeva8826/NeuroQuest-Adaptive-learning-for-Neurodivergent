import logging
from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from bson import ObjectId
from app.models.user import UserRegister, UserLogin, Token, UserResponse
from app.database import get_database
from app.services.auth_service import (
    get_password_hash, verify_password, create_access_token, get_current_user
)

logger = logging.getLogger("neuroquest.routers.auth")

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/register", response_model=Token)
async def register(user_data: UserRegister):
    db = get_database()
    
    # Check if email exists
    existing_user = await db["users"].find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address already registered."
        )
        
    hashed_pwd = get_password_hash(user_data.password)
    full_name = user_data.full_name or user_data.username
    
    user_doc = {
        "email": user_data.email,
        "username": user_data.username,
        "password_hash": hashed_pwd,
        "full_name": full_name,
        "role": user_data.role,
        "created_at": datetime.utcnow()
    }
    
    result = await db["users"].insert_one(user_doc)
    user_id = str(result.inserted_id)
    
    # Create associated learner profile document if role is caregiver
    learner_id = None
    if user_data.role == "caregiver":
        learner_name = user_data.learner_name or f"{full_name}'s Learner"
        learner_doc = {
            "caregiver_id": user_id,
            "name": learner_name,
            "age": user_data.learner_age,
            "condition": user_data.primary_condition or "Not Specified",
            "created_at": datetime.utcnow()
        }
        learner_res = await db["learners"].insert_one(learner_doc)
        learner_id = str(learner_res.inserted_id)
        
        # Link learner_id to user
        await db["users"].update_one(
            {"_id": result.inserted_id},
            {"$set": {"learner_id": learner_id}}
        )

    # Issue JWT token
    access_token = create_access_token(data={"sub": user_data.email, "role": user_data.role})
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        user_id=user_id,
        role=user_data.role,
        email=user_data.email,
        full_name=user_data.full_name,
        learner_id=learner_id,
        has_completed_onboarding=False,
        has_completed_medical=False
    )

@router.post("/login", response_model=Token)
@router.post("/token", response_model=Token)
async def login(credentials: UserLogin):
    db = get_database()
    identifier = credentials.email or credentials.username
    if not identifier:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email is required."
        )
    logger.info(f"[AUTH_DEBUG] Login attempt for identifier: '{identifier}'")
    user = await db["users"].find_one({
        "$or": [
            {"email": {"$regex": f"^{identifier}$", "$options": "i"}},
            {"username": {"$regex": f"^{identifier}$", "$options": "i"}}
        ]
    })
    logger.info(f"[AUTH_DEBUG] Mongo lookup result: {user is not None}")
    if not user:
        try:
            from app.database import SessionLocal
            from app.models.schema import User as SqlUser
            from sqlalchemy import func, or_
            if SessionLocal is not None:
                sql_session = SessionLocal()
                try:
                    sql_u = sql_session.query(SqlUser).filter(
                        or_(
                            func.lower(SqlUser.email) == identifier.lower(),
                            func.lower(SqlUser.username) == identifier.lower()
                        )
                    ).first()
                    logger.info(f"[AUTH_DEBUG] SQL lookup result: {sql_u is not None}")
                    if sql_u:
                        is_match = verify_password(credentials.password, sql_u.hashed_password) or \
                                   (credentials.password in ["123", "1234"] and verify_password("1234", sql_u.hashed_password)) or \
                                   (credentials.password in ["123", "1234"] and verify_password("123", sql_u.hashed_password))
                        logger.info(f"[AUTH_DEBUG] SQL password match: {is_match}")
                        if is_match:
                            l_doc = await db["learners"].find_one({"caregiver_id": str(sql_u.id)})
                            if not l_doc:
                                l_res = await db["learners"].insert_one({
                                    "caregiver_id": str(sql_u.id),
                                    "name": f"{sql_u.username}'s Learner",
                                    "created_at": datetime.utcnow()
                                })
                                learner_id = str(l_res.inserted_id)
                            else:
                                learner_id = str(l_doc["_id"])
                            user = {
                                "email": sql_u.email,
                                "username": sql_u.username,
                                "password_hash": sql_u.hashed_password,
                                "full_name": sql_u.username,
                                "role": sql_u.role.value if hasattr(sql_u.role, 'value') else str(sql_u.role),
                                "learner_id": learner_id,
                                "created_at": datetime.utcnow()
                            }
                            res = await db["users"].insert_one(user)
                            user["_id"] = res.inserted_id
                            logger.info(f"[AUTH_DEBUG] Seeded user into Mongo from SQL: {user.get('email')}")
                finally:
                    sql_session.close()
        except Exception as e:
            logger.error(f"[AUTH_DEBUG] SQL fallback exception: {e}")

    pw_match = False
    if user:
        stored_hash = user.get("password_hash") or user.get("hashed_password") or ""
        if stored_hash:
            pw_match = verify_password(credentials.password, stored_hash)
            if not pw_match:
                # Grace check for demo passwords (123 vs 1234 or Password123!)
                if (credentials.password in ["123", "1234"] and verify_password("1234", stored_hash)) or \
                   (credentials.password in ["123", "1234"] and verify_password("123", stored_hash)) or \
                   (credentials.password in ["Password123!", "password", "Pass123!"] and verify_password("Password123!", stored_hash)):
                    pw_match = True
                    # Auto-update hash
                    try:
                        new_h = get_password_hash(credentials.password)
                        await db["users"].update_one({"_id": user["_id"]}, {"$set": {"password_hash": new_h}})
                    except Exception:
                        pass
        logger.info(f"[AUTH_DEBUG] User found, pw_match={pw_match}")
    else:
        logger.info(f"[AUTH_DEBUG] User is None after all checks")

    if not user or not pw_match:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
        
    user_id = str(user["_id"])
    learner_id = user.get("learner_id")
    
    # Check if onboarding and medical completed
    has_completed_onboarding = False
    has_completed_medical = False
    if learner_id:
        pref = await db["learner_preferences"].find_one({"learner_id": learner_id})
        has_completed_onboarding = pref is not None
        
        med_prof = await db["medical_profiles"].find_one({"learner_id": learner_id})
        has_completed_medical = med_prof is not None
        
    access_token = create_access_token(data={"sub": user["email"], "role": user["role"]})
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        user_id=user_id,
        role=user["role"],
        email=user["email"],
        full_name=user.get("full_name", user["username"]),
        learner_id=learner_id,
        has_completed_onboarding=has_completed_onboarding,
        has_completed_medical=has_completed_medical
    )

@router.post("/reset-password")
async def reset_password_api(payload: dict):
    identifier = (payload.get("identifier") or payload.get("email") or payload.get("username") or "").strip().lower()
    new_password = payload.get("new_password") or payload.get("password")
    if not identifier:
        raise HTTPException(status_code=400, detail="Username or email is required")
    if not new_password or len(new_password) < 3:
        raise HTTPException(status_code=400, detail="Password must be at least 3 characters")

    db = get_database()
    new_hash = get_password_hash(new_password)
    found = False

    # 1. Update in SQL if exists
    try:
        from app.database import SessionLocal
        from app.models.schema import User as SqlUser
        from sqlalchemy import or_, func
        if SessionLocal is not None:
            sql_session = SessionLocal()
            try:
                sql_u = sql_session.query(SqlUser).filter(
                    or_(func.lower(SqlUser.username) == identifier, func.lower(SqlUser.email) == identifier)
                ).first()
                if sql_u:
                    sql_u.hashed_password = new_hash
                    sql_session.commit()
                    found = True
            finally:
                sql_session.close()
    except Exception:
        pass

    # 2. Update in MongoDB
    if db is not None:
        res = await db["users"].update_many(
            {"$or": [
                {"email": {"$regex": f"^{identifier}$", "$options": "i"}},
                {"username": {"$regex": f"^{identifier}$", "$options": "i"}}
            ]},
            {"$set": {"password_hash": new_hash}}
        )
        if res.matched_count > 0:
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="No account found with this username or email.")

    return {"message": "Password updated successfully! You can now log in."}

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    db = get_database()
    learner_id = current_user.get("learner_id")
    has_completed_onboarding = False
    has_completed_medical = False
    if learner_id:
        pref = await db["learner_preferences"].find_one({"learner_id": learner_id})
        has_completed_onboarding = pref is not None
        
        med_prof = await db["medical_profiles"].find_one({"learner_id": learner_id})
        has_completed_medical = med_prof is not None
        
    return UserResponse(
        id=current_user["id"],
        email=current_user["email"],
        username=current_user["username"],
        full_name=current_user["full_name"],
        role=current_user["role"],
        learner_id=learner_id,
        has_completed_onboarding=has_completed_onboarding,
        has_completed_medical=has_completed_medical,
        created_at=current_user.get("created_at", datetime.utcnow())
    )
