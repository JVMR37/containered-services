from pydantic import BaseModel

from application.entities.serializers.extra import Extra


class OrderItemExtraBase(BaseModel):
    extra_id: int


class OrderItemExtraCreate(OrderItemExtraBase):
    pass


class OrderItemExtra(OrderItemExtraBase):
    id: int
    order_item_id: int
    extra: Extra

    class Config:
        orm_mode = True
