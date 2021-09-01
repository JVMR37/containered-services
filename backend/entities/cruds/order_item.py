from sqlalchemy.orm import Session

from backend.entities.database.models import OrderItem as dbOrderItem
from backend.entities.serializers import OrderItemCreate


def get_by_id(db: Session, order_item_id: int):
    return db.query(dbOrderItem).filter(dbOrderItem.id == order_item_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dbOrderItem).offset(skip).limit(limit).all()


def get_by_order_id(db: Session, order_id: int, skip: int = 0, limit: int = 100):
    return db.query(dbOrderItem).filter(dbOrderItem.order_id == order_id).offset(skip).limit(limit).all()


def create(db: Session, order_id: int, order_item: OrderItemCreate):
    instance = dbOrderItem(order_id=order_id, item_id=order_item.item_id, amount=order_item.amount,
                           notes=order_item.notes, combo=order_item.combo)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def update_by_id(db: Session, order_item_id: int, order_item: OrderItemCreate):
    rows: int = db.query(dbOrderItem).filter(
        dbOrderItem.id == order_item_id).update(order_item.dict())
    db.commit()
    return rows


def delete_by_order_id(db: Session, order_id: int):
    rows: int = db.query(dbOrderItem).filter(
        dbOrderItem.order_id == order_id).delete()
    db.commit()
    return rows


def delete_by_id(db: Session, order_item_id: int):
    rows: int = db.query(dbOrderItem).filter(
        dbOrderItem.id == order_item_id).delete()
    db.commit()
    return rows
