import enum

from sqlalchemy import Column, Enum, Integer, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class ItemType(enum.Enum):
    BOOK = "book"
    MOVIE = "movie"
    SERIE = "serie"

class ItemStatus(enum.Enum):
    TO_WATCH = "to_watch"
    WATCHING = "watching"
    WATCHED = "watched"

class EmisionStatus(enum.Enum):
    NOT_EMITED = "not_emited"
    EMITING = "emiting"
    EMITED = "emited"
    
class Item(Base):
    __tablename__ = "items"

    id             = Column(Integer, primary_key=True, index=True)
    type           = Column(Enum(ItemType), nullable=False)
    status         = Column(Enum(ItemStatus), nullable=False)
    emision_status = Column(Enum(EmisionStatus), nullable=False)
    is_favorite    = Column(Boolean, default=False)
    book           = relationship("Book", back_populates="item")
    movie          = relationship("Movie", back_populates="item")
    serie          = relationship("Serie", back_populates="item")
    sagas          = relationship("SagaItem", back_populates="item")
    comments       = relationship("Comment", back_populates="item")
    genres         = relationship("ItemGenre", back_populates="item")
