from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone

class Comment(Base):
    __tablename__ = "comments"

    id          = Column(Integer, primary_key=True, index=True)
    item_id     = Column(Integer, ForeignKey("items.id"), nullable=False)
    content     = Column(String(1000), nullable=False)
    created_at  = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    item        = relationship("Item", back_populates="comments")