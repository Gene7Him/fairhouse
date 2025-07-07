from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as connection:
    connection.execute(text("""
        ALTER TABLE properties
        ADD COLUMN IF NOT EXISTS accountability_score FLOAT;
    """))
    print("✅ accountability_score column added to properties table.")
