from sqlalchemy.orm import Session

from backend.entities.database.models import Extra as dbExtra
from backend.entities.serializers import ExtraCreate


def get_by_id(db: Session, extra_id: int):
    return db.query(dbExtra).filter(dbExtra.id == extra_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dbExtra).offset(skip).limit(limit).all()


def create(db: Session, extra: ExtraCreate):
    instance = dbExtra(name=extra.name, price=extra.price)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def delete_by_id(db: Session, extra_id: int):
    instance = get_by_id(db, extra_id=extra_id)
    if instance is None:
        return None

    db.delete(instance)
    db.commit()
    return instance
