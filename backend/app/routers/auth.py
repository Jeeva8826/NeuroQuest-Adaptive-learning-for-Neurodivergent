from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from bson import ObjectId
from app.models.user import UserRegister, UserLogin, Token, UserResponse
from app.database import get_database
from app.services.auth_service import (
    get_password_hash, verify_password, create_access_token, get_current_user
)

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
    user = await db["users"].find_one({"$or": [{"email": identifier}, {"username": identifier}]})
    if not user or not verify_password(credentials.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password."
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
        full_name=user["full_name"],
        learner_id=learner_id,
        has_completed_onboarding=has_completed_onboarding,
        has_completed_medical=has_completed_medical
    )

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
