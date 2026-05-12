from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.serie import SerieCreate, SerieResponse, SeasonResponse, TMDBSerieResult
from app.models.serie import Serie
from app.services.tmdb import search_tv_shows

router = APIRouter(prefix="/api/series", tags=["series"])

@router.get("/", response_model=list[SerieResponse])
async def get_series(db: Session = Depends(get_db)):
    db_series = db.query(Serie).all()
    return db_series

@router.get("/search", response_model=list[TMDBSerieResult])
async def search_series(query: str, db: Session = Depends(get_db)):
    data = await search_tv_shows(query)
    return data["results"]

@router.get("/{serie_id}", response_model=SerieResponse)
def get_serie(serie_id: int, db: Session = Depends(get_db)):
    db_serie = db.query(Serie).filter(Serie.id == serie_id).first()
    if not db_serie:
        raise HTTPException(status_code=404, detail="Serie not found")
    return db_serie

@router.get("/{serie_id}/seasons", response_model=list[SeasonResponse])
def get_serie_seasons(serie_id: int, db: Session = Depends(get_db)):
    db_serie = db.query(Serie).filter(Serie.id == serie_id).first()
    if not db_serie:
        raise HTTPException(status_code=404, detail="Serie not found")
    return db_serie.seasons

@router.post("/", response_model=SerieResponse)
def create_serie(serie: SerieCreate, db: Session = Depends(get_db)):
    db_serie = Serie(**serie.model_dump())
    db.add(db_serie)
    db.commit()
    db.refresh(db_serie)
    return db_serie

@router.put("/{serie_id}", response_model=SerieResponse)
def update_serie(serie_id: int, serie: SerieCreate, db: Session = Depends(get_db)):
    db_serie = db.query(Serie).filter(Serie.id == serie_id).first()
    if not db_serie:
        raise HTTPException(status_code=404, detail="Serie not found")
    for key, value in serie.model_dump().items():
        setattr(db_serie, key, value)
    db.commit()
    db.refresh(db_serie)
    return db_serie

@router.delete("/{serie_id}", status_code=204)
def delete_serie(serie_id: int, db: Session = Depends(get_db)):
    db_serie = db.query(Serie).filter(Serie.id == serie_id).first()
    if not db_serie:
        raise HTTPException(status_code=404, detail="Serie not found")
    db.delete(db_serie)
    db.commit()