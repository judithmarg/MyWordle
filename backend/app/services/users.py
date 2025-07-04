from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.users import UserResponse, UserCreateRequest, UserUpdateRequest

def get_all_users(db: Session):
    try:
        return db.query(User).all()
    except:
        raise ValueError("Bad connection with User Table in Database")

def get_user_by_id(user_id: int, db: Session):
    user_db = db.query(User).filter(User.id == user_id).first()
    if not user_db:
        raise ValueError("There's not an user with requested id.")
    return user_db

def create_user_service(user_data: UserCreateRequest, db: Session):
    all_users = get_all_users(db)
    existent_user = any(user.username == user_data.username for user in all_users)
    if existent_user:
        raise ValueError("You can't create a user again with the same username.")
    try:
        new_user = User(
            username = user_data.username,
            password = user_data.password,
            email= user_data.email
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    except IntegrityError:
        db.rollback()
        raise ValueError("You can't create a user with the same username.")
    
    except Exception as e:
        db.rollback()
        raise RuntimeError("Unexpected error while saving user.") from e

def update_user_service(user_id: int, user_data: UserUpdateRequest, db: Session):
    user = get_user_by_id(user_id=user_id, db=db)
    if not user:
        return None
    
    for field, value in user_data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

def delete_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise ValueError("There's not an user with requested username.")
    
    db.delete(user)
    db.commit()
    return { "message": f"User {username} removed succesfully!"}



