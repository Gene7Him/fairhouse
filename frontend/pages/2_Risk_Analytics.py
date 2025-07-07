import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Risk Analytics", layout="wide")
st.title("📊 Risk Analytics")

# ⛽ Connect to Neon
DATABASE_URL = st.secrets["DATABASE_URL"]

@st.cache_data
def load_data():
    engine = create_engine(DATABASE_URL)
    df = pd.read_sql("SELECT * FROM properties", engine)
    return df

df = load_data()

if "accountability_score" not in df.columns:
    st.warning("No scores found. Please run the scoring script.")
else:
    zip_scores = (
        df.groupby("zip_code")["accountability_score"]
        .mean()
        .reset_index()
        .sort_values("accountability_score")
    )
    st.subheader("📉 Average Accountability Score by ZIP Code")
    st.bar_chart(zip_scores.set_index("zip_code"))
