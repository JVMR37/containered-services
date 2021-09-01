from sqlalchemy.orm import Session

from backend.entities.database.models import Item as dbItem
from backend.entities.serializers import ItemCreate


def get_by_id(db: Session, item_id: int):
    return db.query(dbItem).filter(dbItem.id == item_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dbItem).offset(skip).limit(limit).all()


def create(db: Session, item: ItemCreate):
    instance = dbItem(name=item.name, price=item.price,
                      price_combo=item.price_combo)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def delete_by_id(db: Session, item_id: int):
    instance = get_by_id(db, item_id=item_id)
    if instance is None:
        return None

    db.delete(instance)
    db.commit()
    return instance
