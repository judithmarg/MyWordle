from fastapi import HTTPException
from sqlalchemy.orm import Session
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
    existent_user = filter(lambda user: user.username == user_data.username, all_users)
    if len(list(existent_user)) > 0:
        raise ValueError("You can't create a user again with the same username.")

    new_user = User(
        username = user_data.username,
        password = user_data.password,
        email= user_data.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_service(user_id: int, user_data: UserUpdateRequest, db: Session):
    user = get_user_by_id(user_id=user_id, db=db)
    user["username"] = user_data.username
    user["password"] = user_data.password

    db.commit()
    db.refresh(user)
    return user

def delete_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise ValueError("There's not an user with requested username.")
    
    db.delete(user)
    db.commit()
    db.refresh(user)
    return { "message": f"User {username} removed succesfully!"}



