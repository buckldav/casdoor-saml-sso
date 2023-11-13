from .config import CONFIG

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(CONFIG.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    """
    Dependency
    Usage: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-tables
    def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        db_user = crud.get_user_by_email(db, email=user.email)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
