from sqlalchemy import String, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class University(Base):
    __tablename__ = "universities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))

    country = relationship("Country", back_populates="universities")
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())