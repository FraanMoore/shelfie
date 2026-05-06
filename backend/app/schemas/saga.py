from pydantic import BaseModel

class SagaBase(BaseModel):
    name: str
    type: str
    cover: str | None = None

class SagaCreate(SagaBase):
    pass

class SagaResponse(SagaBase):
    id: int
    
    class Config:
        from_attributes = True

class ItemSagaBase(BaseModel):
    order: int

class ItemSagaCreate(ItemSagaBase):
    pass

class ItemSagaResponse(ItemSagaBase):
    saga_id: int
    item_id: int

    class Config:
        from_attributes = True