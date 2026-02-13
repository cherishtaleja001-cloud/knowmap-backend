from pydantic import BaseModel


# ---------------- USER ----------------

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# ---------------- DATASET ----------------

class DatasetCreate(BaseModel):
    name: str
    description: str


class DatasetResponse(BaseModel):
    id: int
    name: str
    description: str
    user_id: int

    class Config:
        from_attributes = True
