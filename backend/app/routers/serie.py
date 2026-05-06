from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.serie import SerieCreate, SerieResponse, SeasonResponse

router = APIRouter(prefix="/api/series", tags=["series"])

@router.get("/", response_model=list[SerieResponse])
def get_series(db: Session = Depends(get_db)):
    pass

@router.get("/{serie_id}", response_model=SerieResponse)
def get_serie(serie_id: int, db: Session = Depends(get_db)):
    pass

@router.get("/{serie_id}/seasons", response_model=list[SeasonResponse])
def get_serie_seasons(serie_id: int, db: Session = Depends(get_db)):
    pass

@router.post("/", response_model=SerieResponse)
def create_serie(serie: SerieCreate, db: Session = Depends(get_db)):
    pass

@router.put("/{serie_id}", response_model=SerieResponse)
def update_serie(serie_id: int, serie: SerieCreate, db: Session = Depends(get_db)):
    pass

@router.delete("/{serie_id}", status_code=204)
def delete_serie(serie_id: int, db: Session = Depends(get_db)):
    pass