from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_score(landlord_id: str):
    return {
        "landlord_id": landlord_id,
        "accountability_score": 72  # Placeholder score
    }
