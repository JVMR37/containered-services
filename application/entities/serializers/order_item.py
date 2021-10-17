from typing import List, Optional

from pydantic import BaseModel

from application.entities.serializers.item import Item
from application.entities.serializers.order_item_extra import OrderItemExtra


class OrderItemBase(BaseModel):
    item_id: int
    amount: int
    notes: Optional[str] = None
    combo: Optional[bool] = False


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int
    order_id: int
    item: Item
    extras: List[OrderItemExtra] = []

    class Config:
        orm_mode = True
