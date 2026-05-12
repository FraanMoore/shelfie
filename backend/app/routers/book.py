from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import BookCreate, BookResponse, OpenLibraryBookResult
from app.models.book import Book
from app.services.open_library import search_books as ol_search_books, get_book_details as ol_get_book_details

router = APIRouter(prefix="/api/books", tags=["books"])

@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@router.get("/search", response_model=list[OpenLibraryBookResult])
async def search_books(query: str):
    data = await ol_search_books(query)
    return data["docs"]
 
@router.get("/openlibrary/{book_id}", response_model=OpenLibraryBookResult)
async def get_book_details(book_id: str):
    data = await ol_get_book_details(book_id)
    return data

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.model_dump().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()