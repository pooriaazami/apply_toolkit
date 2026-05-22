from sqlalchemy import select

from ..models import Tag, Professor

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