from sqlalchemy.orm import Session
from app import models, schemas


def register_user(user: schemas.UserCreate, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        return None

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password  # (Later we will hash it)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(user: schemas.UserLogin, db: Session):
    return db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password
    ).first()
