# データベースの構造

from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base

class Brand(Base):
    __tablename__ = 'brands'
    brand_id  = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String, unique=True, index=True)

class State(Base):
    __tablename__ = 'states'
    state_id  = Column(Integer, primary_key=True, index=True)
    state_name = Column(String, unique=True, index=True)

class Taste(Base):
    __tablename__ = 'tastes'
    taste_id  = Column(Integer, primary_key=True, index=True)
    taste_name = Column(String, unique=True, index=True)

class Item(Base):
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, unique=True, index=True)
    brand_id = Column(Integer, ForeignKey('brands.brand_id', ondelete='SET NULL'), nullable=False)
    state_id = Column(Integer, ForeignKey('states.state_id', ondelete='SET NULL'), nullable=False)
    taste_id = Column(Integer, ForeignKey('tastes.taste_id', ondelete='SET NULL'), nullable=False)
    item_bfl = Column(Integer)
    item_price = Column(Integer)
