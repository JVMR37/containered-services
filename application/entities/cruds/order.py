from typing import Optional

from sqlalchemy.orm import Session

from application.entities.database.models import Order as dbOrder
from application.entities.serializers import OrderCreate, OrderUpdate


def get_by_id(db: Session, order_id: int):
    return db.query(dbOrder).filter(dbOrder.id == order_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100, done: Optional[bool] = None):
    if done is None:
        return db.query(dbOrder).offset(skip).limit(limit).all()

    return db.query(dbOrder).filter(dbOrder.done == done).offset(skip).limit(limit).all()


def create(db: Session, order: OrderCreate):
    instance = dbOrder(customer=order.customer)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def update_by_id(db: Session, order: OrderUpdate, order_id: int):
    rows = 0
    if order.done is not None:
        rows: int = db.query(dbOrder).filter(
            dbOrder.id == order_id).update({dbOrder.done: order.done})

    if order.customer is not None:
        rows: int = db.query(dbOrder).filter(dbOrder.id == order_id).update(
            {dbOrder.customer: order.customer})

    db.commit()
    return rows


def delete_by_id(db: Session, order_id: int):
    rows: int = db.query(dbOrder).filter(dbOrder.id == order_id).delete()
    db.commit()
    return rows
