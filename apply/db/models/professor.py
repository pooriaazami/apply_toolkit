from sqlalchemy import String, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class FieldOfStudy(Base):
    ...

class Professor(Base):
    ...
