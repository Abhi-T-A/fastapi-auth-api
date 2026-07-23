from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Any, Dict

class SignUpRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)

class UserResponse(BaseModel):
    id: str
    email: str
    created_at: Optional[str] = None

class AuthResponse(BaseModel):
    message: str
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    user: Optional[UserResponse] = None

class ErrorResponse(BaseModel):
    error: str