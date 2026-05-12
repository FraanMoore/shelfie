from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.movie import MovieCreate, MovieResponse, TMDBMovieResult
from app.models.movie import Movie
from app.services.tmdb import search_movies as tmdb_search_movies

router = APIRouter(prefix="/api/movies", tags=["movies"])

@router.get("/", response_model=list[MovieResponse])
async def get_movies(db: Session = Depends(get_db)):
    db_movies = db.query(Movie).all()
    return db_movies

@router.get("/search", response_model=list[TMDBMovieResult])
async def search_movies(query: str, db: Session = Depends(get_db)):
    data = await tmdb_search_movies(query)
    return data["results"]

@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/", response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    for key, value in movie.model_dump().items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_movie)
    db.commit()