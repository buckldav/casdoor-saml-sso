from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .orm import orm_create_user
from settings.database import get_db
from .models import UserCreate
from .mail import send_signup_email

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("")
def list_users(db: Session = Depends(get_db)):
    return {"users": 0}


@router.post("")
async def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user = orm_create_user(db, user_create)
    if user_create.email is not None:
        await send_signup_email(user_create.email)
    return {"name": user.name}
