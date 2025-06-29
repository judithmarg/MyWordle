from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.users import UserResponse, UserCreateRequest, UserUpdateRequest
from app.services.users import create_user_service, update_user_service, delete_user_by_username, get_user_by_id

router = APIRouter(prefix="/users")

@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreateRequest, db: Session=Depends(get_db)):
    response = create_user_service(user_data, db)
    if not response:
        raise HTTPException(status_code=404, detail="Bad response while trying to create user.")
    return response

@router.get("/{user_id}", response_model=UserResponse)
def create_user(user_id: int, db: Session=Depends(get_db)):
    response = get_user_by_id(user_id=user_id, db=db)
    if not response:
        raise HTTPException(status_code=404, detail="Bad response while trying to get specific user.")
    return response

@router.put("/{user_id}", response_model=UserResponse)
def create_user(user_id: int, user_data: UserUpdateRequest, db: Session=Depends(get_db)):
    response = update_user_service(user_id, user_data, db)
    if not response:
        raise HTTPException(status_code=404, detail="Bad response while trying to update user.")
    return response

@router.delete("/{username}")
def delete_user(username: str, db: Session=Depends(get_db)):
    deleted_user = delete_user_by_username(username, db)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="Bad response with deleted user")
    return deleted_user