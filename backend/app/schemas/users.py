from pydantic import BaseModel
from datetime import datetime

class UserCreateRequest(BaseModel):
    username: str
    password: str
    email: str

class UserUpdateRequest(BaseModel):
    password: str
    email: str

class UserResponse(UserCreateRequest):
    id: int
    created_at: datetime