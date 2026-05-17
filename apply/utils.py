import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv('.env')

def create_db_connection():
    engine = create_engine(
        'sqlite:///' + os.getenv("DATABASE_PATH", "apply_db.sqlite3"),
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
