import os

import typer

from db.models import User
from utils import create_db_connection

from dotenv import load_dotenv

load_dotenv('.env')

def create_database():
    SessionLocal = create_db_connection()
    session = SessionLocal()

    User.metadata.create_all(bind=session.get_bind())


def main():
    if os.path.exists(os.environ.get("DATABASE_PATH", "apply_db.sqlite3")):
        typer.echo("Database already exists. Skipping creation.")
    else:
        typer.echo("Creating database...")
        create_database()
        typer.echo("Database created successfully.")

if __name__ == "__main__":
    main()