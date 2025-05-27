from fastapi import FastAPI
from backend.api.endpoints import properties, scores

app = FastAPI(
    title="FairHouse API",
    description="Backend for the FairHouse housing justice platform.",
    version="0.1.0"
)

app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(scores.router, prefix="/scores", tags=["Scoring"])
