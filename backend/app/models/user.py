from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: Optional[str] = None
    role: str = "caregiver" # caregiver or learner
    learner_name: Optional[str] = None
    learner_age: Optional[int] = None
    primary_condition: Optional[str] = None # Added for medical onboarding

class UserLogin(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: str
    role: str
    email: str
    full_name: Optional[str] = ""
    learner_id: Optional[str] = None
    has_completed_onboarding: bool = False
    has_completed_medical: bool = False # Added for medical onboarding

class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    full_name: Optional[str] = ""
    role: str
    learner_id: Optional[str] = None
    has_completed_onboarding: bool = False
    has_completed_medical: bool = False # Added for medical onboarding
    created_at: datetime
