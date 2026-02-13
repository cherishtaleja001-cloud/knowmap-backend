from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, get_db
from app import models, schemas, auth

# -------------------------------
# Create database tables
# -------------------------------
Base.metadata.create_all(bind=engine)

app = FastAPI(title="KnowMap Backend API")


# -------------------------------
# Enable CORS (STEP 6)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------
# Home Route
# -------------------------------
@app.get("/")
def home():
    return {"message": "KnowMap Backend Running 🚀"}


# -------------------------------
# USER REGISTRATION
# -------------------------------
@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = auth.register_user(user, db)

    if not new_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return new_user


# -------------------------------
# USER LOGIN
# -------------------------------
@app.post("/login", response_model=schemas.UserResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    existing_user = auth.login_user(user, db)

    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return existing_user


# -------------------------------
# CREATE DATASET
# -------------------------------
@app.post("/datasets/{user_id}", response_model=schemas.DatasetResponse)
def create_dataset(
    user_id: int,
    dataset: schemas.DatasetCreate,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_dataset = models.Dataset(
        name=dataset.name,
        description=dataset.description,
        user_id=user_id
    )

    db.add(new_dataset)
    db.commit()
    db.refresh(new_dataset)

    return new_dataset
