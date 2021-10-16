from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.entities.cruds import item as items
from backend.entities.serializers import Item, ItemCreate
from backend.routers.dependencies import get_db
from backend.routers.user import RoleChecker

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=Item, dependencies=[Depends(RoleChecker(['admin']))])
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return items.create(db, item=item)


@router.get("", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return items.get_all(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    instance = items.get_by_id(db, item_id=item_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return instance


@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    instance = items.delete_by_id(db, item_id=item_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return instance
