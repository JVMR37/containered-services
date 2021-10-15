from sqlalchemy.orm import Session

from backend.entities.database.models import User as dbUser
from backend.entities.serializers import UserCreate


def get_by_id(db: Session, user_id: int):
    return db.query(dbUser).filter(dbUser.id == user_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dbUser).offset(skip).limit(limit).all()


def create(db: Session, user: UserCreate):
    instance = dbUser(
        name=user.name,
        email=user.email,
        password=user.password,
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def delete_by_id(db: Session, user_id: int):
    instance = get_by_id(db, user_id=user_id)
    if instance is None:
        return None

    db.delete(instance)
    db.commit()
    return instance
