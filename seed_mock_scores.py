import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import random

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

# Load properties
df = pd.read_sql("SELECT * FROM properties", engine)

# Assign random scores
df["accountability_score"] = [random.randint(0, 100) for _ in range(len(df))]

# Overwrite the table
df.to_sql("properties", engine, if_exists="replace", index=False)
print("✅ Properties updated with mock scores.")
