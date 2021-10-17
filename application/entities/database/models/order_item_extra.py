from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from application.entities.database.config import Base


class OrderItemExtra(Base):
    __tablename__ = "order_item_extras"
    id = Column(Integer, primary_key=True, index=True)
    order_item_id = Column(Integer, ForeignKey(
        "order_items.id", ondelete='CASCADE'))
    extra_id = Column(Integer, ForeignKey("extras.id"))

    order_item = relationship("OrderItem", back_populates="extras")
    extra = relationship("Extra", back_populates="order_item_extra")
