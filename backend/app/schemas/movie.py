from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    director: str
    year: int
    cover: str | None = None

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int
    item_id: int
    
    class Config:
        from_attributes = True

class TMDBMovieResult(BaseModel):
    id: int
    title: str
    release_date: str | None = None
    overview: str | None = None
    poster_path: str | None = None