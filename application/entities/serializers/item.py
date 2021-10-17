from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float
    price_combo: float


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
