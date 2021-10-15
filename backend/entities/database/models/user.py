from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime

from backend.entities.database.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(DateTime, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
