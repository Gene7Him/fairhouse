from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.core.models import Property
from backend.services.scoring_engine import compute_accountability_score

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_score(property_id: int, db: Session = Depends(get_db)):
    # Fetch property from DB
    property_obj = db.query(Property).filter(Property.property_id == property_id).first()
    if not property_obj:
        raise HTTPException(status_code=404, detail="Property not found")

    # Compute the score
    score = compute_accountability_score(
        owner_name=property_obj.owner_name,
        last_sale_price=property_obj.last_sale_price
    )

    # Return the result
    return {
        "property_id": property_obj.property_id,
        "owner_name": property_obj.owner_name,
        "last_sale_price": property_obj.last_sale_price,
        "accountability_score": score
    }
