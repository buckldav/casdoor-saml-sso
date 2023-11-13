from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings.database import get_db
from .models import UserCreate

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("")
def list_users(db: Session = Depends(get_db)):
    return {"users": 0}


@router.post("")
def create_user(user: UserCreate):
    return {}
