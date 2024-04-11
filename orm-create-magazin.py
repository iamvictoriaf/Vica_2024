from sqlalchemy import Table, Index, Integer, String, \
    Column, Text, DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, create_engine, Numeric

from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime

engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db3")
session = Session(bind=engine)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    update_on = Column(DateTime, default=datetime.now, onupdate=datetime.now())
    orders = relationship('Order')

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10,2), nullable=False)
    seling_price = Column(Numeric(10, 2), nullable=False)
    count = Column(Integer)
