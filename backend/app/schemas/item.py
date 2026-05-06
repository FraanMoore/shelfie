from pydantic import BaseModel
from app.models.item import ItemType, ItemStatus, EmisionStatus

class ItemBase(BaseModel):
    type: ItemType
    status: ItemStatus
    emision_status: EmisionStatus
    is_favorite: bool = False

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True