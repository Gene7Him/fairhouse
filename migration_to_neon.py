import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Use Neon connection
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Upload properties
properties_path = "data/raw/sample_properties_geocoded.csv"
if os.path.exists(properties_path):
    properties_df = pd.read_csv(properties_path)
    properties_df["sale_date"] = pd.to_datetime(properties_df["sale_date"])
    properties_df.to_sql("properties", engine, if_exists="replace", index=False)
    print("✅ Properties table uploaded.")
else:
    print("⚠️ sample_properties_geocoded.csv not found.")

# Upload reports (optional)
reports_path = "data/reports.csv"
if os.path.exists(reports_path):
    reports_df = pd.read_csv(reports_path)
    reports_df["timestamp"] = pd.to_datetime(reports_df["timestamp"])
    reports_df.to_sql("reports", engine, if_exists="replace", index=False)
    print("✅ Reports table uploaded.")
else:
    print("⚠️  No reports.csv found — skipping report upload.")
