from sqlalchemy import select

from ..models import University, Country

def add_university(session, name: str, country: str):
    country_obj = session.query(Country).filter_by(name=country).first()
    university = University(name=name, country_id=country_obj.id)

    session.add(university)
    session.commit()

def get_universities_by_country(session, country_id: int):
    return session.query(University).filter_by(country_id=country_id).all()

def get_universities_by_user(session, user_id: int):
    return session.scalar(
            select(University)
            .join(University.country) 
            .where(Country.user_id == user_id)
    ).all()