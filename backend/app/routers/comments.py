from app.models.comment import Comment

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.comment import CommentCreate, CommentResponse
from app.models.item import Item

router = APIRouter(prefix="/api/items/{item_id}/comments", tags=["comments"])

@router.get("/", response_model=list[CommentResponse])
def get_comments(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    comments = db.query(Comment).filter(Comment.item_id == item_id).all()
    return comments

@router.post("/", response_model=CommentResponse)
def create_comment(item_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_comment = Comment(**comment.model_dump(), item_id=item_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.delete("/{comment_id}", status_code=204)
def delete_comment(item_id: int, comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id, Comment.item_id == item_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(db_comment)
    db.commit()