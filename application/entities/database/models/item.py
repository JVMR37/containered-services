from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from application.entities.database.config import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    price_combo = Column(Float)

    order_item = relationship("OrderItem", back_populates="item")
