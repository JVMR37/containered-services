from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from backend.entities.database.config import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    done_at = Column(DateTime, nullable=True)
    done = Column(Boolean, default=False)

    items = relationship(
        "OrderItem", back_populates="order", cascade="all,delete")
