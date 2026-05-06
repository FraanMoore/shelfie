from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    cover: str | None = None

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    item_id: int
    
    class Config:
        from_attributes = True