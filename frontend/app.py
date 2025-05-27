import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="FairHouse Dashboard", layout="wide")

st.title("🏡 FairHouse: Housing Accountability Dashboard")

# -- Load property data from your CSV or backend
@st.cache_data
def load_data():
    # For now, load from CSV (until API pagination is added)
    df = pd.read_csv("data/raw/sample_properties.csv")
    return df

df = load_data()

# -- Show raw data
st.subheader("📋 All Properties")
st.dataframe(df)

# -- Select a property and fetch its accountability score from the backend
property_id = st.selectbox("🏷️ Select Property ID to Score", df.index + 1)
selected = df.iloc[property_id - 1]

# -- Request score from your FastAPI
url = f"http://localhost:8000/scores/?property_id={property_id}"
response = requests.get(url)

if response.status_code == 200:
    score_data = response.json()
    st.metric(label=f"Accountability Score for {selected['owner_name']}", value=score_data["accountability_score"])
else:
    st.warning("Could not fetch score from API.")

# -- Optional: Map View (color by price as placeholder)
st.subheader("🗺️ Risk Zone Map (mock)")
if "zip_code" in df.columns:
    st.map(df.assign(lat=37.77, lon=-122.41))  # Mock SF location for now
