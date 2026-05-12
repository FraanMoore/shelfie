from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.saga import SagaCreate, SagaResponse
from app.models.saga import Saga

router = APIRouter(prefix="/api/sagas", tags=["sagas"])

@router.get("/", response_model=list[SagaResponse])
def get_sagas(db: Session = Depends(get_db)):
    db_sagas = db.query(Saga).all()
    return db_sagas

@router.get("/{saga_id}", response_model=SagaResponse)
def get_saga(saga_id: int, db: Session = Depends(get_db)):
    db_saga = db.query(Saga).filter(Saga.id == saga_id).first()
    if not db_saga:
        raise HTTPException(status_code=404, detail="Saga not found")
    return db_saga

@router.post("/", response_model=SagaResponse)
def create_saga(saga: SagaCreate, db: Session = Depends(get_db)):
    db_saga = Saga(**saga.model_dump())
    db.add(db_saga)
    db.commit()
    db.refresh(db_saga)
    return db_saga

@router.put("/{saga_id}", response_model=SagaResponse)
def update_saga(saga_id: int, saga: SagaCreate, db: Session = Depends(get_db)):
    db_saga = db.query(Saga).filter(Saga.id == saga_id).first()
    if not db_saga:
        raise HTTPException(status_code=404, detail="Saga not found")
    for key, value in saga.model_dump().items():
        setattr(db_saga, key, value)
    db.commit()
    db.refresh(db_saga)
    return db_saga

@router.delete("/{saga_id}", status_code=204)
def delete_saga(saga_id: int, db: Session = Depends(get_db)):
    db_saga = db.query(Saga).filter(Saga.id == saga_id).first()
    if not db_saga:
        raise HTTPException(status_code=404, detail="Saga not found")
    db.delete(db_saga)
    db.commit()