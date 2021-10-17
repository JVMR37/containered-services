from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from application.routers.dependencies import get_db
from application.entities.serializers import Order, OrderCreate, OrderUpdate
from application.entities.cruds import order as orders

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=Order)
def create_order(order: OrderCreate,  db: Session = Depends(get_db)):
    return orders.create(db, order=order)


@router.patch("/{order_id}", response_model=int)
def update_order(order: OrderUpdate, order_id: int, db: Session = Depends(get_db)):
    rows = orders.update_by_id(db, order=order, order_id=order_id)

    if rows == 0:
        raise HTTPException(status_code=404, detail="Order not found")

    return rows


@router.get("", response_model=List[Order])
def read_orders(skip: int = 0, limit: int = 100, done: Optional[bool] = None, db: Session = Depends(get_db)):
    return orders.get_all(db, skip=skip, limit=limit, done=done)


@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    instance = orders.get_by_id(db, order_id=order_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return instance


@router.delete("/{order_id}", response_model=int)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    rows = orders.delete_by_id(db, order_id=order_id)

    if rows == 0:
        raise HTTPException(status_code=404, detail="Order not found")

    return rows
