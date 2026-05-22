from sqlalchemy import select

from ..models import Country

def add_country(session, name: str, code: str, user_id: int):
    new_country = Country(name=name, code=code, user_id=user_id)
    
    session.add(new_country)
    session.commit()
    session.refresh(new_country)

    return new_country

def get_countries_by_user(session, user_id: int):
    stmt = select(Country).where(Country.user_id == user_id)
    result = session.execute(stmt).scalars().all()
    return result