import pandas as pd
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.core.models import Property

def load_csv_to_db():
    df = pd.read_csv("data/raw/sample_properties.csv")
    db: Session = SessionLocal()

    for _, row in df.iterrows():
        prop = Property(
            address=row["address"],
            zip_code=row["zip_code"],
            owner_name=row["owner_name"],
            last_sale_price=row["last_sale_price"],
            sale_date=row["sale_date"],
        )
        db.add(prop)
    db.commit()
    db.close()

if __name__ == "__main__":
    load_csv_to_db()
