from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.genre import GenreCreate, GenreResponse

router = APIRouter(prefix="/api/genres", tags=["genres"])

@router.get("/", response_model=list[GenreResponse])
def get_genres(db: Session = Depends(get_db)):
    pass

@router.get("/{genre_id}", response_model=GenreResponse)
def get_genre(genre_id: int, db: Session = Depends(get_db)):    
    pass
