from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Genre(Base):
    __tablename__ = "genres"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    items       = relationship("ItemGenre", back_populates="genre")

class ItemGenre(Base):
    __tablename__ = "item_genres"

    item_id     = Column(Integer, ForeignKey("items.id"), primary_key=True)
    genre_id    = Column(Integer, ForeignKey("genres.id"), primary_key=True)
    item        = relationship("Item", back_populates="genres")
    genre       = relationship("Genre", back_populates="items")