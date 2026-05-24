from sqlalchemy import select

from ..models import Tag, Professor, Country, University

def add_tag(session, name: str, user_id: int):
    new_tag = Tag(name=name, user_id=user_id)
    
    session.add(new_tag)
    session.commit()
    session.refresh(new_tag)

    return new_tag

def get_tags_by_user(session, user_id: int):
    stmt = select(Tag).where(Tag.user_id == user_id)
    result = session.execute(stmt).scalars().all()
    return result

def get_professors_by_user(session, user_id: int):
    stmt = select(Professor) \
        .join(University) \
        .join(Country, Country.id == University.country_id) \
        .where(Country.user_id == user_id)
    result = session.execute(stmt).scalars().all()
    return result

def add_professor(session, name: str, email: str, university_id: int, notes: str):
    new_professor = Professor(name=name, email=email, university_id=university_id, notes=notes)
    
    session.add(new_professor)
    session.commit()
    session.refresh(new_professor)

    return new_professor

def add_professor_tags(session, professor_id: int, tag_ids: list[int]):
    professor = session.get(Professor, professor_id)
    if not professor:
        raise ValueError("Professor not found")

    tags = session.query(Tag).filter(Tag.id.in_(tag_ids)).all()
    professor.tags.extend(tags)

    session.commit()