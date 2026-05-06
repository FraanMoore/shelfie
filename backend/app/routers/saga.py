from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.saga import SagaCreate, SagaResponse

router = APIRouter(prefix="/api/sagas", tags=["sagas"])

@router.get("/", response_model=list[SagaResponse])
def get_sagas(db: Session = Depends(get_db)):
    pass

@router.get("/{saga_id}", response_model=SagaResponse)
def get_saga(saga_id: int, db: Session = Depends(get_db)):
    pass

@router.post("/", response_model=SagaResponse)
def create_saga(saga: SagaCreate, db: Session = Depends(get_db)):
    pass

@router.put("/{saga_id}", response_model=SagaResponse)
def update_saga(saga_id: int, saga: SagaCreate, db: Session = Depends(get_db)):
    pass

@router.delete("/{saga_id}", status_code=204)
def delete_saga(saga_id: int, db: Session = Depends(get_db)):
    pass