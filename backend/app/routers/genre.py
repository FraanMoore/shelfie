from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.genre import GenreResponse
from app.models.genre import Genre

router = APIRouter(prefix="/api/genres", tags=["genres"])

@router.get("/", response_model=list[GenreResponse])
def get_genres(db: Session = Depends(get_db)):
    db_genres = db.query(Genre).all()
    return db_genres

@router.get("/{genre_id}", response_model=GenreResponse)
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre
