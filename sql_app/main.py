from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Read
@app.get('/items', response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get('/brands', response_model=List[schemas.Brand])
async def read_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    brands = crud.get_brands(db, skip=skip, limit=limit)
    return brands

@app.get('/states', response_model=List[schemas.State])
async def read_states(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    states = crud.get_states(db, skip=skip, limit=limit)
    return states

@app.get('/tastes', response_model=List[schemas.Taste])
async def read_tastes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tastes = crud.get_tastes(db, skip=skip, limit=limit)
    return tastes

# Create
@app.post('/items', response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.post('/brands', response_model=schemas.Brand)
async def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db=db, brand=brand)

@app.post('/states', response_model=schemas.State)
async def create_state(state: schemas.StateCreate, db: Session = Depends(get_db)):
    return crud.create_state(db=db, state=state)

@app.post('/tastes', response_model=schemas.Taste)
async def create_taste(taste: schemas.TasteCreate, db: Session = Depends(get_db)):
    return crud.create_taste(db=db, taste=taste)

# Update
@app.put('/items/{item_id}')
async def update_item(item_id: int, new_data: dict, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item_id=item_id, new_data=new_data)

# Delete
@app.delete('/items/{item_id}')
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db=db, item_id=item_id)

