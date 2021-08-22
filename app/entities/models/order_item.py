from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.entities.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    amount = Column(Integer)
    notes = Column(Text)
    combo = Column(Boolean, default=False)

    order = relationship("Order", back_populates="items")
    item = relationship("Item", back_populates="order_item")
