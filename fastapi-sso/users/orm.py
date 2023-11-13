from sqlalchemy.orm import Session

from . import models


def orm_get_user(db: Session, user_id: int):
    return db.query(models.UserORM).filter(models.UserORM.id == user_id).first()


def orm_get_user_by_email(db: Session, email: str):
    return db.query(models.UserORM).filter(models.UserORM.email == email).first()


def orm_get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserORM).offset(skip).limit(limit).all()


def orm_create_user(db: Session, user_create: models.UserCreate):
    user = models.User(**user_create.model_dump())
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserORM(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: models.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
