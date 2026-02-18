from fastapi import HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from models import User
from repositories.user_repo import UserRepo
from schemas.user_schema import UserSchema
router = APIRouter()

@router.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    New_user=User(email=user.email,password=user.password)
    user_repo.add_user(New_user)
    return {"message": "User signed up successfully"}

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    users=user_repo.get_all_users()
    return users

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user=user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user