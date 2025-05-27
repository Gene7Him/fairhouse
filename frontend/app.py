import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

st.set_page_config(page_title="FairHouse Dashboard", layout="wide")

st.title("🏡 FairHouse: Housing Accountability Dashboard")

# Load geocoded property data
@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/sample_properties_geocoded.csv")
    return df.dropna(subset=["latitude", "longitude"])

df = load_data()

# Get scores from API
@st.cache_data
def fetch_scores(df):
    scores = []
    for _, row in df.iterrows():
        try:
            res = requests.get(f"http://localhost:8000/scores/?property_id={row['property_id']}")
            if res.status_code == 200:
                score = res.json().get("accountability_score", 0)
            else:
                score = 0
        except:
            score = 0
        scores.append(score)
    df["accountability_score"] = scores
    return df

df = fetch_scores(df)

# Score to RGB
def score_to_color(score):
    r = int(255 - (score * 2.55))
    g = int(score * 2.55)
    return [r, g, 0]

df["color"] = df["accountability_score"].apply(score_to_color)

# Sidebar filters
st.sidebar.header("🔍 Filter Properties")
zip_filter = st.sidebar.multiselect("Zip Code", options=sorted(df["zip_code"].unique()), default=df["zip_code"].unique())
owner_filter = st.sidebar.text_input("Owner Name Contains")
score_min, score_max = st.sidebar.slider("Accountability Score Range", 0, 100, (0, 100))

filtered_df = df[
    (df["zip_code"].isin(zip_filter)) &
    (df["accountability_score"].between(score_min, score_max)) &
    (df["owner_name"].str.contains(owner_filter, case=False, na=False))
]

# Map display
st.subheader("🗺️ Properties Colored by Accountability Score")

layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_df,
    get_position='[longitude, latitude]',
    get_color="color",
    get_radius=100,
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=filtered_df["latitude"].mean(),
    longitude=filtered_df["longitude"].mean(),
    zoom=10,
    pitch=0
)

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[layer],
    tooltip={"text": "Owner: {owner_name}\nScore: {accountability_score}"}
))

# Data table
st.subheader("📋 Property Details")
st.dataframe(filtered_df[[
    "property_id", "address", "zip_code", "owner_name", "accountability_score"
]])

st.subheader("📉 ZIP Code Risk Overview")

zip_scores = (
    filtered_df.groupby("zip_code")["accountability_score"]
    .mean()
    .reset_index()
    .sort_values("accountability_score")
)

st.bar_chart(zip_scores.set_index("zip_code"))

import os
from datetime import datetime

st.subheader("📣 Report Housing Misconduct")

with st.form("report_form"):
    selected_id = st.selectbox("Select Property ID", df["property_id"])
    issue_type = st.selectbox("Issue Type", ["Rent Hike", "Unsafe Conditions", "Eviction Threat", "Harassment", "Other"])
    description = st.text_area("Describe the issue")
    reporter_name = st.text_input("Your Name (optional)")
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        report = {
            "timestamp": datetime.now().isoformat(),
            "property_id": selected_id,
            "issue_type": issue_type,
            "description": description,
            "reporter_name": reporter_name or "Anonymous"
        }
        reports_file = "data/reports.csv"
        os.makedirs("data", exist_ok=True)

        if os.path.exists(reports_file):
            existing = pd.read_csv(reports_file)
            df_new = pd.concat([existing, pd.DataFrame([report])], ignore_index=True)
        else:
            df_new = pd.DataFrame([report])

        df_new.to_csv(reports_file, index=False)
        st.success("✅ Report submitted successfully.")

st.subheader("🧾 Recent Reports")

if os.path.exists("data/reports.csv"):
    st.dataframe(pd.read_csv("data/reports.csv").sort_values("timestamp", ascending=False))
else:
    st.info("No reports yet.")
