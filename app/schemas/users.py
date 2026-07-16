from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    name: str = Field(max_length=30)
    email: EmailStr

class UserCreate(UserBase):
    None #потом добавить пароль?

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=30)
    name: Optional[str] = Field(None, max_length=30)
    email: Optional[EmailStr] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime