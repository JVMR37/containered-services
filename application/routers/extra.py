from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from application.routers.dependencies import get_db
from application.entities.serializers import Extra, ExtraCreate
from application.entities.cruds import extra as extras
from application.routers.user import RoleChecker


router = APIRouter(
    prefix="/extras",
    tags=["extras"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=Extra, dependencies=[Depends(RoleChecker(['admin']))])
def create_extra(extra: ExtraCreate,  db: Session = Depends(get_db)):
    return extras.create(db, extra=extra)


@router.put("", response_model=Extra, dependencies=[Depends(RoleChecker(['admin']))])
def create_extra_put(extra: ExtraCreate,  db: Session = Depends(get_db)):
    return extras.create(db, extra=extra)


@router.get("", response_model=List[Extra])
def read_extras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return extras.get_all(db, skip=skip, limit=limit)


@router.get("/{extra_id}", response_model=Extra)
def read_extra(extra_id: int, db: Session = Depends(get_db)):
    instance = extras.get_by_id(db, extra_id=extra_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="Extra not found")

    return instance


@router.delete("/{extra_id}", response_model=Extra, dependencies=[Depends(RoleChecker(['admin']))])
def delete_extra(extra_id: int, db: Session = Depends(get_db)):
    instance = extras.delete_by_id(db, extra_id=extra_id)
    if instance is None:
        raise HTTPException(status_code=404, detail="Extra not found")

    return instance
