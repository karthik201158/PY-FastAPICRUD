from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#database dialect (mysql) and the driver (pymysql)
DATABASE_URL = "mysql+pymysql://root:123456@localhost/fastapi"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
