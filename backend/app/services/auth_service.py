from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import settings
from app.database import get_database

import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        # Fallback to passlib verify if needed
        try:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            return pwd_context.verify(plain_password, hashed_password)
        except Exception:
            return False

def get_password_hash(password: str) -> str:
    # Use bcrypt directly for 100% compatibility on Python 3.13
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        sub = payload.get("sub")
        email = payload.get("email", sub)
        username = payload.get("username", sub)
        if not sub:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    db = get_database()
    user = None
    if db is not None:
        user = await db["users"].find_one({
            "$or": [
                {"email": email},
                {"username": username},
                {"email": sub},
                {"username": sub}
            ]
        })

    # Fallback to check SQLAlchemy user if not found in MongoDB
    if user is None:
        try:
            from app.database import SessionLocal
            from app.models.schema import User as SqlUser
            if SessionLocal is not None:
                sql_session = SessionLocal()
                try:
                    sql_u = sql_session.query(SqlUser).filter(
                        (SqlUser.email == email) | (SqlUser.username == username) | (SqlUser.username == sub) | (SqlUser.email == sub)
                    ).first()
                    if sql_u:
                        learner_id = f"learner_{sql_u.id}"
                        if db is not None:
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
                            "id": str(sql_u.id),
                            "username": sql_u.username,
                            "email": sql_u.email,
                            "role": sql_u.role.value if hasattr(sql_u.role, 'value') else str(sql_u.role),
                            "learner_id": learner_id
                        }
                        if db is not None:
                            user_mongo = user.copy()
                            user_mongo["created_at"] = datetime.utcnow()
                            ins_res = await db["users"].insert_one(user_mongo)
                            user["_id"] = ins_res.inserted_id
                finally:
                    sql_session.close()
        except Exception:
            pass

    if user is None:
        raise credentials_exception

    # Convert _id to string id and ensure user_id and learner_id are available
    if "_id" not in user and "id" in user:
        user["_id"] = user["id"]
    user["id"] = str(user.get("_id", user.get("id", "")))
    user["user_id"] = user["id"]

    if not user.get("learner_id") and db is not None:
        l_doc = await db["learners"].find_one({"$or": [{"caregiver_id": user["id"]}, {"caretaker_id": user["id"]}]})
        if l_doc:
            user["learner_id"] = str(l_doc.get("_id", l_doc.get("id")))
            await db["users"].update_one({"_id": user.get("_id")}, {"$set": {"learner_id": user["learner_id"]}})
        else:
            user["learner_id"] = None

    return user

oauth2_scheme_optional = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)

async def get_optional_current_user(token: Optional[str] = Depends(oauth2_scheme_optional)) -> Optional[dict]:
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        sub = payload.get("sub")
        if not sub:
            return None
        db = get_database()
        if db is None:
            return None
        user = await db["users"].find_one({
            "$or": [
                {"_id": sub},
                {"email": sub},
                {"username": sub},
                {"id": sub}
            ]
        })
        if user:
            user["id"] = str(user.get("_id", user.get("id", "")))
            user["user_id"] = user["id"]
        return user
    except Exception:
        return None

