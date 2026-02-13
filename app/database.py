from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

# 🔐 Put your actual MySQL password inside the quotes
raw_password = "Mukesh@123"

# Encode special characters safely
password = quote_plus(raw_password)

DATABASE_URL = f"mysql+pymysql://root:{password}@localhost/knowmap_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

