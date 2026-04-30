from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Saga(Base):
    __tablename__ = "sagas"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    type        = Column(String, nullable=False)
    cover       = Column(String, nullable=True)
    items       = relationship("SagaItem", back_populates="saga")

class SagaItem(Base):
    __tablename__ = "saga_items"

    id          = Column(Integer, primary_key=True, index=True)
    saga_id     = Column(Integer, ForeignKey("sagas.id"), nullable=False)
    item_id     = Column(Integer, ForeignKey("items.id"), nullable=False)
    order       = Column(Integer, nullable=False)
    saga        = relationship("Saga", back_populates="items")
    item        = relationship("Item", back_populates="sagas")