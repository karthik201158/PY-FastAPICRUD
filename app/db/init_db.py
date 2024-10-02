from app.db.session import engine
from app.db.base import Base

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
