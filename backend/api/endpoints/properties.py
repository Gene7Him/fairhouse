from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.core.models import Property

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_properties(zip_code: str = None, db: Session = Depends(get_db)):
    query = db.query(Property)
    if zip_code:
        query = query.filter(Property.zip_code == zip_code)
    results = query.limit(100).all()
    return [p.__dict__ for p in results]
