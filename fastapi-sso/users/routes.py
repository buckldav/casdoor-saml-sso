from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .orm import orm_create_user
from settings.database import get_db
from .models import UserCreate

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("")
def list_users(db: Session = Depends(get_db)):
    return {"users": 0}


@router.post("")
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user = orm_create_user(db, user_create)
    return {"name": user.name}
