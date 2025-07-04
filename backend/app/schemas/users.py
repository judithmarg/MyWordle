from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserCreateRequest(BaseModel):
    username: str
    password: str
    email: str

    class Config:
        from_attributes = True

class UserUpdateRequest(BaseModel):
    password: Optional[str] = ""
    email: Optional[str] = ""

class UserResponse(UserCreateRequest):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True