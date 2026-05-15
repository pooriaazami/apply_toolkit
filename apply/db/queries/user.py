from sqlalchemy import func, select

from ..utils import hash_password
from ..models.user import User


def get_number_of_users(session):
    return session.scalar(
        select(func.count()).select_from(User)
    )

def create_user(session, username: str, password: str):
    password_hash = hash_password(password)
    new_user = User(username=username, password_hash=password_hash)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return new_user