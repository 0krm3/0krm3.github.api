from sqlalchemy.orm import Session
from . import models, schemas

# ブランド一覧取得
def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()

# 形態一覧取得
def get_states(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.State).offset(skip).limit(limit).all()

# 味一覧取得
def get_tastes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Taste).offset(skip).limit(limit).all()

# 商品一覧取得
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


# ブランド登録
def create_brand(db: Session, brand: schemas.Brand):
    db_brand = models.Brand(brand_name=brand.brand_name)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

# 形態登録
def create_state(db: Session, state: schemas.State):
    db_state = models.State(state_name=state.state_name)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

# 味登録
def create_taste(db: Session, taste: schemas.Taste):
    db_taste = models.Taste(taste_name=taste.taste_name)
    db.add(db_taste)
    db.commit()
    db.refresh(db_taste)
    return db_taste

# 商品登録
def create_item(db: Session, item: schemas.Item):
    db_item = models.Item(
        item_name = item.item_name,
        brand_id = item.brand_id,
        state_id = item.state_id,
        taste_id = item.taste_id,
        item_bfl = item.item_bfl,
        item_price = item.item_price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# 商品更新
def update_item(db: Session, item_id: int, new_data: dict):
    db_item = db.query(models.Item).filter(models.Item.item_id == item_id).one()
    for key, value in new_data.items():
        setattr(db_item, key, value)
    if new_data:
        db.commit()
    return db_item


# 商品削除
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.item_id == item_id).one()
    db.delete(db_item)
    db.commit()
    return db_item