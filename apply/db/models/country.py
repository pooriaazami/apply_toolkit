from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    code: Mapped[str] = mapped_column(String(2), unique=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    universities = relationship("University", back_populates="country")