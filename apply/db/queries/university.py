from sqlalchemy import select

from ..models import University, Country

def add_university(session, name: str, country_id: int):
    new_university = University(name=name, country_id=country_id)

    session.add(new_university)
    session.commit()
    session.refresh(new_university)

    return new_university

def get_universities_by_country(session, country_id: int):
    return session.query(University).filter_by(country_id=country_id).all()

def get_universities_by_user(session, user_id: int):
    return session.scalar(
            select(University)
            .join(University.country) 
            .where(Country.user_id == user_id)
    ).all()