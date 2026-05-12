from pydantic import BaseModel

class SerieBase(BaseModel):
    title: str
    director: str
    year: int
    cover: str | None = None
    has_seasons: bool = False

class SerieCreate(SerieBase):
    pass

class SerieResponse(SerieBase):
    id: int
    item_id: int
    
    class Config:
        from_attributes = True

class SeasonBase(BaseModel):
    season_name: str
    year: int
    cover: str | None = None
    director: str
    order: int

class SeasonCreate(SeasonBase):
    pass

class SeasonResponse(SeasonBase):
        serie_id: int

        class Config:
            from_attributes = True

class TMDBSerieResult(BaseModel):
    id: int
    name: str
    first_air_date: str | None = None
    overview: str | None = None
    poster_path: str | None = None