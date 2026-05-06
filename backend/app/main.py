from fastapi import FastAPI
from app.routers import book, genre, item, comments, movie, saga, serie

app = FastAPI()
app.include_router(book.router)
app.include_router(genre.router)
app.include_router(item.router)
app.include_router(comments.router)
app.include_router(movie.router)
app.include_router(saga.router)
app.include_router(serie.router)