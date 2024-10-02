from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import product as product_schema
from app.crud import product as crud_product
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=product_schema.Product)
def create_product(
    product_in: product_schema.ProductCreate, db: Session = Depends(get_db)
):
    return crud_product.create_product(db=db, product=product_in)