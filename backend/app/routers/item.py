from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.item import ItemCreate, ItemResponse
from app.models.item import Item
from app.models.genre import Genre, ItemGenre

router = APIRouter(prefix="/api/items", tags=["items"])

@router.get("/", response_model=list[ItemResponse])
def get_items(
        type: str | None = None,
        status: str | None = None,
        is_favorite: bool | None = None,
        genre: str | None = None,
        db: Session = Depends(get_db),
):
    query = db.query(Item)
    if type:
        query = query.filter(Item.type == type)
    if status:
        query = query.filter(Item.status == status)
    if is_favorite is not None:
        query = query.filter(Item.is_favorite == is_favorite)
    if genre:
        query = query.join(ItemGenre, Item.id == ItemGenre.item_id)
        query = query.join(Genre, ItemGenre.genre_id == Genre.id)
        query = query.filter(Genre.name == genre)

    items = query.all()
    return items


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()