from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id          = Column(Integer, primary_key=True, index=True)
    item_id     = Column(Integer, ForeignKey("items.id"), nullable=False)
    title       = Column(String, nullable=False)
    director    = Column(String, nullable=False)
    year        = Column(Integer, nullable=False)
    cover       = Column(String, nullable=True)
    item        = relationship("Item", back_populates="movie")