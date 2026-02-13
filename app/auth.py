from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def register_user(user: schemas.UserCreate, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(user: schemas.UserLogin, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not existing_user or existing_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return existing_user
