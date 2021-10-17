from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from application.routers.dependencies import get_db
from application.entities.serializers import OrderItemExtra, OrderItemExtraCreate
from application.entities.cruds import order_item_extra as order_item_extras

router = APIRouter(
    prefix="/orders/{order_id}/items/{order_item_id}/extras",
    tags=["order-item-extras"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=OrderItemExtra)
def create_order_item_extra(order_id: int, order_item_id: int, order_item_extra: OrderItemExtraCreate,
                            db: Session = Depends(get_db)):
    return order_item_extras.create(db, order_item_id=order_item_id, order_item_extra=order_item_extra)


@router.put("", response_model=OrderItemExtra)
def create_order_item_extra_put(order_id: int, order_item_id: int, order_item_extra: OrderItemExtraCreate,
                                db: Session = Depends(get_db)):
    return order_item_extras.create(db, order_item_id=order_item_id, order_item_extra=order_item_extra)


@router.patch("/{order_item_extra_id}", response_model=int)
def update_order_item_extra(order_id: int, order_item_id: int, order_item_extra_id: int,
                            order_item_extra: OrderItemExtraCreate, db: Session = Depends(get_db)):
    return order_item_extras.update_by_id(db, order_item_extra_id=order_item_extra_id,
                                          order_item_extra=order_item_extra)


@router.put("/{order_item_extra_id}", response_model=int)
def update_order_item_extra_put(order_id: int, order_item_id: int, order_item_extra_id: int,
                                order_item_extra: OrderItemExtraCreate, db: Session = Depends(get_db)):
    return order_item_extras.update_by_id(db, order_item_extra_id=order_item_extra_id,
                                          order_item_extra=order_item_extra)


@router.get("", response_model=List[OrderItemExtra])
def read_order_item_extras(order_id: int, order_item_id: int, skip: int = 0, limit: int = 100,
                           db: Session = Depends(get_db)):
    instances = order_item_extras.get_by_order_item_id(
        db, order_item_id=order_item_id, skip=skip, limit=limit)
    if instances is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return instances


@router.get("/{order_item_extra_id}", response_model=OrderItemExtra)
def read_order_item_extra(order_id: int, order_item_id: int, order_item_extra_id: int, db: Session = Depends(get_db)):
    instance = order_item_extras.get_by_id(
        db, order_item_extra_id=order_item_extra_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return instance


@router.delete("", response_model=int)
def delete_order_item_extras(order_id: int, order_item_id: int, db: Session = Depends(get_db)):
    rows = order_item_extras.delete_by_order_item_id(
        db, order_item_id=order_item_id)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows


@router.delete("/{order_item_extra_id}", response_model=int)
def delete_order_item_extra(order_id: int, order_item_id: int, order_item_extra_id: int, db: Session = Depends(get_db)):
    rows = order_item_extras.delete_by_id(
        db, order_item_extra_id=order_item_extra_id)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows
