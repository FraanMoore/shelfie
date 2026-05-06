from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.comment import CommentCreate, CommentResponse

router = APIRouter(prefix="/api/items/{item_id}/comments", tags=["comments"])

@router.get("/", response_model=list[CommentResponse])
def get_comments(item_id: int, db: Session = Depends(get_db)):
    pass

@router.post("/", response_model=CommentResponse)
def create_comment(item_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    pass

@router.delete("/{comment_id}", status_code=204)
def delete_comment(item_id: int, comment_id: int, db: Session = Depends(get_db)):
    pass