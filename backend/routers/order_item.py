from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.routers.dependencies import get_db
from backend.entities.serializers import OrderItem, OrderItemCreate
from backend.entities.cruds import order_item as order_items

router = APIRouter(
    prefix="/orders/{order_id}/items",
    tags=["order-items"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=OrderItem)
def create_order_item(order_id: int, order_item: OrderItemCreate, db: Session = Depends(get_db)):
    return order_items.create(db, order_id, order_item)


@router.put("", response_model=OrderItem)
def create_order_item_put(order_id: int, order_item: OrderItemCreate, db: Session = Depends(get_db)):
    return order_items.create(db, order_id, order_item)


@router.patch("/{order_item_id}", response_model=int)
def update_order_item(order_id: int, order_item_id: int, order_item: OrderItemCreate,
                      db: Session = Depends(get_db)):
    return order_items.update_by_id(db, order_item_id=order_item_id, order_item=order_item)


@router.put("/{order_item_id}", response_model=int)
def update_order_item_put(order_id: int, order_item_id: int, order_item: OrderItemCreate,
                          db: Session = Depends(get_db)):
    return order_items.update_by_id(db, order_item_id=order_item_id, order_item=order_item)


@router.get("", response_model=List[OrderItem])
def read_order_items(order_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return order_items.get_by_order_id(db, order_id=order_id, skip=skip, limit=limit)


@router.get("/{order_item_id}", response_model=OrderItem)
def read_order_item(order_id: int, order_item_id: int, db: Session = Depends(get_db)):
    instance = order_items.get_by_id(db, order_item_id=order_item_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return instance


@router.delete("", response_model=int)
def delete_order_items(order_id: int, db: Session = Depends(get_db)):
    rows = order_items.delete_by_order_id(db, order_id=order_id)
    return rows


@router.delete("/{order_item_id}", response_model=int)
def delete_order_item(order_id: int, order_item_id: int, db: Session = Depends(get_db)):
    rows = order_items.delete_by_id(db, order_item_id=order_item_id)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows
