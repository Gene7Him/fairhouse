from backend.core.database import engine
from backend.core.models import Base

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
