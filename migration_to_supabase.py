import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_DB_URL")
engine = create_engine(SUPABASE_URL)

# Upload properties
properties_df = pd.read_csv("data/raw/sample_properties_geocoded.csv")
properties_df["sale_date"] = pd.to_datetime(properties_df["sale_date"])
properties_df.to_sql("properties", engine, if_exists="append", index=False)
print("✅ Properties table uploaded.")

# Upload reports (only if file exists)
if os.path.exists("data/reports.csv"):
    reports_df = pd.read_csv("data/reports.csv")
    reports_df["timestamp"] = pd.to_datetime(reports_df["timestamp"])
    reports_df.to_sql("reports", engine, if_exists="replace", index=False)
    print("✅ Reports table uploaded.")
else:
    print("⚠️  No reports.csv found — skipping report upload.")
