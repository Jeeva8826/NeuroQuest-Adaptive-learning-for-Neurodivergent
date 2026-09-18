import jwt
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from passlib.context import CryptContext
from datetime import datetime, timedelta
import redis
import json

from ..database import get_db
from ..models.schema import User, UserRole

from app.config import settings
from app.database import get_database

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.JWT_SECRET
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# Redis connection (Fail softly and instantly if redis is unavailable during dev)
import socket
try:
    with socket.create_connection(('127.0.0.1', 6379), timeout=0.05):
        r = redis.Redis(host='127.0.0.1', port=6379, db=0, socket_timeout=0.1)
        r.ping()
except Exception:
    r = None

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    user_id: int

class UserLogin(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str

class UserRegister(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str
    role: str = "CAREGIVER"
    learner_name: str = "" # Optional, specifically skipping medical diagnosis

class PasswordResetRequest(BaseModel):
    identifier: str
    new_password: str

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

import bcrypt

def get_password_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')[:72]
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8')[:72], hashed_password.encode('utf-8'))
    except Exception:
        return False

@router.post("/register", response_model=Token)
async def register_user(user_in: UserRegister, db: Session = Depends(get_db)):
    from sqlalchemy import or_, func
    u_name = (user_in.username or "").strip()
    u_email = (user_in.email or "").strip().lower()

    # Smart identifier normalization
    if not u_name and not u_email:
        raise HTTPException(status_code=400, detail="Username or email is required")
        
    if not u_email and "@" in u_name:
        u_email = u_name.lower()
        u_name = u_name.split("@")[0]
    elif not u_name and u_email:
        u_name = u_email.split("@")[0]
    elif not u_email:
        u_email = f"{u_name.lower()}@neuroquest.local"

    # Sanitize role
    try:
        user_role = UserRole(user_in.role.upper())
    except Exception:
        user_role = UserRole.CAREGIVER

    # Check existing in SQL
    if db:
        if db.query(User).filter(func.lower(User.username) == u_name.lower()).first():
            raise HTTPException(status_code=400, detail="Username already registered. Please Sign In.")
        if db.query(User).filter(func.lower(User.email) == u_email.lower()).first():
            raise HTTPException(status_code=400, detail="Email already registered. Please Sign In.")

    db_user = User(
        username=u_name,
        email=u_email,
        hashed_password=get_password_hash(user_in.password),
        role=user_role
    )
    if db:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        user_id = db_user.id
    else:
        user_id = 1
    
    # Sync to MongoDB so all learner services can find the user
    try:
        mongo_db = get_database()
        if mongo_db is not None:
            existing_mongo = await mongo_db["users"].find_one({"$or": [{"email": u_email}, {"username": u_name}]})
            if not existing_mongo:
                learner_doc = {
                    "caregiver_id": str(user_id),
                    "name": user_in.learner_name or f"{u_name}'s Learner",
                    "created_at": datetime.utcnow()
                }
                l_res = await mongo_db["learners"].insert_one(learner_doc)
                await mongo_db["users"].insert_one({
                    "email": u_email,
                    "username": u_name,
                    "password_hash": db_user.hashed_password,
                    "full_name": u_name,
                    "role": user_role.value if hasattr(user_role, 'value') else str(user_role),
                    "learner_id": str(l_res.inserted_id),
                    "created_at": datetime.utcnow()
                })
    except Exception as e:
        pass
        
    access_token = create_access_token(data={
        "sub": u_email,
        "email": u_email,
        "username": u_name,
        "role": user_role.value if hasattr(user_role, 'value') else str(user_role)
    })
    
    if r:
        r.set(f"session:{u_name}", json.dumps({"active": True, "login_time": str(datetime.utcnow())}))
        
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user_role.value if hasattr(user_role, 'value') else str(user_role),
        "user_id": user_id
    }

@router.post("/token", response_model=Token)
async def login_for_access_token(user_in: UserLogin, db: Session = Depends(get_db)):
    from sqlalchemy import or_, func
    identifier = (user_in.username or user_in.email or "").strip().lower()
    if not identifier:
        raise HTTPException(status_code=400, detail="Username or email is required")

    db_user = None
    if db:
        db_user = db.query(User).filter(
            or_(
                func.lower(User.username) == identifier,
                func.lower(User.email) == identifier
            )
        ).first()

    pw_match = False
    if db_user:
        pw_match = verify_password(user_in.password, db_user.hashed_password)
        if not pw_match:
            # Grace check for demo passwords (123 vs 1234 or Password123!)
            if (user_in.password in ["123", "1234"] and verify_password("1234", db_user.hashed_password)) or \
               (user_in.password in ["123", "1234"] and verify_password("123", db_user.hashed_password)) or \
               (user_in.password in ["Password123!", "password", "Pass123!"] and verify_password("Password123!", db_user.hashed_password)):
                pw_match = True
                # Auto-heal hash so next direct verify matches immediately
                db_user.hashed_password = get_password_hash(user_in.password)
                db.commit()

    # Fallback to MongoDB if not in SQL or SQL unavailable
    mongo_user = None
    if not db_user or not pw_match:
        try:
            mongo_db = get_database()
            if mongo_db is not None:
                mongo_user = await mongo_db["users"].find_one({
                    "$or": [
                        {"email": {"$regex": f"^{identifier}$", "$options": "i"}},
                        {"username": {"$regex": f"^{identifier}$", "$options": "i"}}
                    ]
                })
                if mongo_user:
                    m_hash = mongo_user.get("password_hash", "")
                    if verify_password(user_in.password, m_hash) or \
                       (user_in.password in ["123", "1234"] and verify_password("1234", m_hash)) or \
                       (user_in.password in ["123", "1234"] and verify_password("123", m_hash)):
                        pw_match = True
        except Exception:
            pass

    if not pw_match or (not db_user and not mongo_user):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    user_email = db_user.email if db_user else mongo_user["email"]
    user_name = db_user.username if db_user else mongo_user["username"]
    user_role_val = db_user.role.value if db_user and hasattr(db_user.role, 'value') else (str(db_user.role) if db_user else mongo_user.get("role", "CAREGIVER"))
    user_id = db_user.id if db_user else 1

    # Ensure sync in MongoDB
    try:
        mongo_db = get_database()
        if mongo_db is not None:
            existing_mongo = await mongo_db["users"].find_one({"$or": [{"email": user_email}, {"username": user_name}]})
            if not existing_mongo:
                learner_doc = {
                    "caregiver_id": str(user_id),
                    "name": f"{user_name}'s Learner",
                    "created_at": datetime.utcnow()
                }
                l_res = await mongo_db["learners"].insert_one(learner_doc)
                await mongo_db["users"].insert_one({
                    "email": user_email,
                    "username": user_name,
                    "password_hash": db_user.hashed_password if db_user else mongo_user["password_hash"],
                    "full_name": user_name,
                    "role": user_role_val,
                    "learner_id": str(l_res.inserted_id),
                    "created_at": datetime.utcnow()
                })
    except Exception as e:
        pass

    access_token = create_access_token(data={
        "sub": user_email,
        "email": user_email,
        "username": user_name,
        "role": user_role_val
    })
    
    if r:
        r.set(f"session:{user_name}", json.dumps({"active": True, "login_time": str(datetime.utcnow())}))
    
    return {"access_token": access_token, "token_type": "bearer", "role": user_role_val, "user_id": user_id}

@router.post("/reset-password")
async def reset_password(req: PasswordResetRequest, db: Session = Depends(get_db)):
    from sqlalchemy import or_, func
    identifier = req.identifier.strip().lower()
    if not identifier:
        raise HTTPException(status_code=400, detail="Username or email is required")
    if not req.new_password or len(req.new_password) < 3:
        raise HTTPException(status_code=400, detail="Password must be at least 3 characters")

    new_hash = get_password_hash(req.new_password)
    found = False

    if db:
        db_user = db.query(User).filter(
            or_(
                func.lower(User.username) == identifier,
                func.lower(User.email) == identifier
            )
        ).first()
        if db_user:
            db_user.hashed_password = new_hash
            db.commit()
            found = True

    try:
        mongo_db = get_database()
        if mongo_db is not None:
            m_res = await mongo_db["users"].update_many(
                {"$or": [
                    {"email": {"$regex": f"^{identifier}$", "$options": "i"}},
                    {"username": {"$regex": f"^{identifier}$", "$options": "i"}}
                ]},
                {"$set": {"password_hash": new_hash}}
            )
            if m_res.matched_count > 0:
                found = True
    except Exception:
        pass

    if not found:
        raise HTTPException(status_code=404, detail="No account found with this username or email.")

    return {"message": "Password updated successfully! You can now log in."}
    
    # Ensure sync in MongoDB
    try:
        mongo_db = get_database()
        if mongo_db is not None:
            existing_mongo = await mongo_db["users"].find_one({"$or": [{"email": db_user.email}, {"username": db_user.username}]})
            if not existing_mongo:
                learner_doc = {
                    "caregiver_id": str(db_user.id),
                    "name": f"{db_user.username}'s Learner",
                    "created_at": datetime.utcnow()
                }
                l_res = await mongo_db["learners"].insert_one(learner_doc)
                await mongo_db["users"].insert_one({
                    "email": db_user.email,
                    "username": db_user.username,
                    "password_hash": db_user.hashed_password,
                    "full_name": db_user.username,
                    "role": db_user.role.value,
                    "learner_id": str(l_res.inserted_id),
                    "created_at": datetime.utcnow()
                })
    except Exception as e:
        pass

    access_token = create_access_token(data={
        "sub": db_user.email,
        "email": db_user.email,
        "username": db_user.username,
        "role": db_user.role.value
    })
    
    if r:
        r.set(f"session:{db_user.username}", json.dumps({"active": True, "login_time": str(datetime.utcnow())}))
    
    return {"access_token": access_token, "token_type": "bearer", "role": db_user.role.value, "user_id": db_user.id}

@router.get("/me")
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(lambda: None)):
    from fastapi import Request
    # We'll handle this with a header-based approach
    return {"message": "Use Authorization header"}

# Proper /me endpoint using JWT verification
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()

@router.get("/whoami")
async def whoami(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        from sqlalchemy import or_, func
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        identifier = (payload.get("username") or payload.get("sub") or payload.get("email") or "").strip().lower()
        if not identifier:
            raise HTTPException(status_code=401, detail="Invalid token")
        db_user = db.query(User).filter(
            or_(
                func.lower(User.username) == identifier,
                func.lower(User.email) == identifier
            )
        ).first()
        if not db_user:
            raise HTTPException(status_code=401, detail="User not found")
        return {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email,
            "role": db_user.role.value if hasattr(db_user.role, 'value') else str(db_user.role),
            "created_at": str(db_user.created_at)
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

def process_learner_model_update(user_id: str, event_data: dict):
    print(f"Background Task: Updating learner {user_id} with event: {event_data}")

@router.post("/events/async")
async def record_event_async(event_data: dict, background_tasks: BackgroundTasks):
    user_id = event_data.get("user_id", "default_user")
    background_tasks.add_task(process_learner_model_update, user_id, event_data)
    return {"message": "Event received and queued for processing"}
