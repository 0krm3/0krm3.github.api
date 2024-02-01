# FastAPI側の構造

from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    item_name: str
    brand_id: int
    state_id: int
    taste_id: int
    item_bfl: int
    item_price: int

class Item(ItemCreate):
    item_id: int

    class Config:
        orm_mode = True


class BrandCreate(BaseModel):
    brand_name: str

class Brand(BrandCreate):
    brand_id: int

    class Config:
        orm_mode = True

class StateCreate(BaseModel):
    state_name: str

class State(StateCreate):
    state_id: int

    class Config:
        orm_mode = True

class TasteCreate(BaseModel):
    taste_name: str

class Taste(TasteCreate):
    taste_id: int

    class Config:
        orm_mode = True
