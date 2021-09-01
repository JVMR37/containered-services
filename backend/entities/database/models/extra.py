from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from backend.entities.database.config import Base


class Extra(Base):
    __tablename__ = "extras"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    price = Column(Float)

    order_item_extra = relationship("OrderItemExtra", back_populates="extra")
