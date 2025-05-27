from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_properties(zip_code: str = None):
    return {
        "message": "Property data will go here.",
        "zip_code": zip_code
    }
