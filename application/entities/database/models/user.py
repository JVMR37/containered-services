from sqlalchemy import Column, Integer, String

from application.entities.database.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    role = Column(String)
    password = Column(String)
