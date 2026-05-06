from pydantic import BaseModel

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreResponse(GenreBase):
    id: int
 
    class Config:
        from_attributes = True

class ItemGenreResponse(BaseModel):
    item_id: int
    genre_id: int
    
    class Config:
        from_attributes = True