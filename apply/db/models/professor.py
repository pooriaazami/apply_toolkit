from sqlalchemy import Column, String, Integer, DateTime, Table, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

professor_tags = Table(
    "professor_tags",
    Base.metadata,
    Column("professor_id", ForeignKey("professors.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    professors: Mapped[list["Professor"]] = relationship(
        "Professor",
        secondary="professor_tags",
        back_populates="tags"
    )

class Professor(Base):
    __tablename__ = "professors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    university_id: Mapped[int] = mapped_column(ForeignKey("universities.id"))
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    notes: Mapped[str] = mapped_column(String(5000), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    
    university = relationship("University")

    tags: Mapped[list["Tag"]] = relationship(
        "Tag",
        secondary="professor_tags",
        back_populates="professors"
    )