from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify length for VARCHAR
    description = Column(String(512), nullable=True)  # Specify length for VARCHAR
    price = Column(Float)
    quantity = Column(Integer)
