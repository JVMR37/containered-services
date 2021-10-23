from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from application.routers.dependencies import get_db
from application.entities.serializers import OrderItem, OrderItemCreate
from application.entities.cruds import order_item as order_items
from application.routers.user import RoleChecker

router = APIRouter(
    prefix="/orders/{order_id}/items",
    tags=["order-items"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=OrderItem, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def create_order_item(order_id: int, order_item: OrderItemCreate, db: Session = Depends(get_db)):
    instance = order_items.create(db, order_id, order_item)
    if instance is None:
        raise HTTPException(
            status_code=404, detail="Check the order id and the item id")

    return instance


@router.put("", response_model=OrderItem, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def create_order_item_put(order_id: int, order_item: OrderItemCreate, db: Session = Depends(get_db)):
    return order_items.create(db, order_id, order_item)


@router.patch("/{order_item_id}", response_model=int, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def update_order_item(order_id: int, order_item_id: int, order_item: OrderItemCreate,
                      db: Session = Depends(get_db)):
    rows = order_items.update_by_id(
        db, order_item_id=order_item_id, order_item=order_item)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows


@router.put("/{order_item_id}", response_model=int, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def update_order_item_put(order_id: int, order_item_id: int, order_item: OrderItemCreate,
                          db: Session = Depends(get_db)):
    rows = order_items.update_by_id(
        db, order_item_id=order_item_id, order_item=order_item)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows


@router.get("", response_model=List[OrderItem], dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def read_order_items(order_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    instances = order_items.get_by_order_id(
        db, order_id=order_id, skip=skip, limit=limit)
    if instances is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return instances


@router.get("/{order_item_id}", response_model=OrderItem, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def read_order_item(order_id: int, order_item_id: int, db: Session = Depends(get_db)):
    instance = order_items.get_by_id(db, order_item_id=order_item_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return instance


@router.delete("", response_model=int, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def delete_order_items(order_id: int, db: Session = Depends(get_db)):
    rows = order_items.delete_by_order_id(db, order_id=order_id)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows


@router.delete("/{order_item_id}", response_model=int, dependencies=[Depends(RoleChecker(['admin', 'caixa']))])
def delete_order_item(order_id: int, order_item_id: int, db: Session = Depends(get_db)):
    rows = order_items.delete_by_id(db, order_item_id=order_item_id)
    if rows == 0:
        raise HTTPException(status_code=404, detail="OrderItem not found")

    return rows
