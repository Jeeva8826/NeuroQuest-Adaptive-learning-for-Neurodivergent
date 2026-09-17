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

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "neuroquest_secure_key_sih2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
    username: str
    email: str
    password: str
    role: str = "CAREGIVER"
    learner_name: str = "" # Optional, specifically skipping medical diagnosis

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
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
    # Check existing
    if db.query(User).filter(User.username == user_in.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
        
    db_user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        role=UserRole(user_in.role)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role.value})
    
    if r:
        r.set(f"session:{db_user.username}", json.dumps({"active": True, "login_time": str(datetime.utcnow())}))
        
    return {"access_token": access_token, "token_type": "bearer", "role": db_user.role.value, "user_id": db_user.id}

@router.post("/token", response_model=Token)
async def login_for_access_token(user_in: UserLogin, db: Session = Depends(get_db)):
    from sqlalchemy import or_, func
    identifier = (user_in.username or user_in.email or "").strip().lower()
    if not identifier:
        raise HTTPException(status_code=400, detail="Username or email is required")

    db_user = db.query(User).filter(
        or_(
            func.lower(User.username) == identifier,
            func.lower(User.email) == identifier
        )
    ).first()
    if not db_user or not verify_password(user_in.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": db_user.username, "role": db_user.role.value})
    
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
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        db_user = db.query(User).filter(User.username == username).first()
        if not db_user:
            raise HTTPException(status_code=401, detail="User not found")
        return {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email,
            "role": db_user.role.value,
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
