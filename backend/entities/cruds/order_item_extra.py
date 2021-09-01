from sqlalchemy.orm import Session

from backend.entities.database.models import OrderItemExtra as dbOrderItemExtra
from backend.entities.serializers import OrderItemExtraCreate


def get_by_id(db: Session, order_item_extra_id: int):
    return db.query(dbOrderItemExtra).filter(dbOrderItemExtra.id == order_item_extra_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dbOrderItemExtra).offset(skip).limit(limit).all()


def get_by_order_item_id(db: Session, order_item_id: int, skip: int = 0, limit: int = 100):
    return db.query(dbOrderItemExtra).filter(dbOrderItemExtra.order_item_id == order_item_id)\
        .offset(skip).limit(limit).all()


def create(db: Session, order_item_id: int, order_item_extra: OrderItemExtraCreate):
    instance = dbOrderItemExtra(
        order_item_id=order_item_id, extra_id=order_item_extra.extra_id)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def update_by_id(db: Session, order_item_extra_id: int, order_item_extra: OrderItemExtraCreate):
    rows: int = db.query(dbOrderItemExtra).filter(
        dbOrderItemExtra.id == order_item_extra_id).update(order_item_extra.dict())
    db.commit()
    return rows


def delete_by_order_item_id(db: Session, order_item_id: int):
    rows: int = db.query(dbOrderItemExtra).filter(
        dbOrderItemExtra.order_item_id == order_item_id).delete()
    db.commit()
    return rows


def delete_by_id(db: Session, order_item_extra_id: int):
    rows: int = db.query(dbOrderItemExtra).filter(
        dbOrderItemExtra.id == order_item_extra_id).delete()
    db.commit()
    return rows
