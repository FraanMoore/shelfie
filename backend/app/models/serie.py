from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Serie(Base):
    __tablename__ = "series"

    id          = Column(Integer, primary_key=True, index=True)
    item_id     = Column(Integer, ForeignKey("items.id"), nullable=False)
    title       = Column(String, nullable=False)
    director    = Column(String, nullable=False)
    year        = Column(Integer, nullable=False)
    cover       = Column(String, nullable=True)
    has_seasons = Column(Boolean, nullable=False)
    item        = relationship("Item", back_populates="serie")
    seasons     = relationship("Season", back_populates="serie")


class Season(Base):
    __tablename__ = "seasons"

    id          = Column(Integer, primary_key=True, index=True)
    serie_id    = Column(Integer, ForeignKey("series.id"), nullable=False)
    season_name = Column(String, nullable=False)
    year        = Column(Integer, nullable=False)
    cover       = Column(String, nullable=True)
    director    = Column(String, nullable=False)
    order       = Column(Integer, nullable=False)
    serie       = relationship("Serie", back_populates="seasons")
