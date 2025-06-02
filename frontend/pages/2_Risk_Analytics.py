import streamlit as st
import pandas as pd

st.title("📊 Risk Analytics")

df = pd.read_csv("../data/raw/sample_properties_geocoded.csv")
if "accountability_score" not in df.columns:
    st.warning("No scores found. Please run the score script.")
else:
    zip_scores = (
        df.groupby("zip_code")["accountability_score"]
        .mean()
        .reset_index()
        .sort_values("accountability_score")
    )
    st.subheader("📉 Average Accountability Score by ZIP Code")
    st.bar_chart(zip_scores.set_index("zip_code"))
