from fastapi import FastAPI
from app.api import product
from app.db.init_db import init_db


app = FastAPI()

# Initialize the database and create tables
init_db()

app.include_router(product.router, prefix="/products", tags=["products"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)