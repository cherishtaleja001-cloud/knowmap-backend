from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models
from . import schemas
from . import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "KnowMap Backend Running 🚀"}


# Register
@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return auth.register_user(user, db)


# Login
@app.post("/login", response_model=schemas.UserResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return auth.login_user(user, db)
