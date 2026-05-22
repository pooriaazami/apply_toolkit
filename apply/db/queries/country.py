from sqlalchemy import select

from ..models import Country

def add_country(session, name: str, code: str, user_id: int):
    new_country = Country(name=name, code=code, user_id=user_id)
    
    session.add(new_country)
    session.commit()
    session.refresh(new_country)

    return new_country

def fetch_all_countries(session):
    scaler = session.scalars(select(Country)).all()
    return list(map(lambda c: f'{str(c.name)} | ({c.code})', scaler))