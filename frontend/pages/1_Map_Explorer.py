import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

st.title("🗺️ Map Explorer")

@st.cache_data
def load_data():
    df = pd.read_csv("../data/raw/sample_properties_geocoded.csv")
    return df.dropna(subset=["latitude", "longitude"])

df = load_data()

@st.cache_data
def fetch_scores(df):
    scores = []
    for _, row in df.iterrows():
        try:
            res = requests.get(f"http://localhost:8000/scores/?property_id={row['property_id']}")
            score = res.json().get("accountability_score", 0) if res.status_code == 200 else 0
        except:
            score = 0
        scores.append(score)
    df["accountability_score"] = scores
    return df

df = fetch_scores(df)

def score_to_color(score):
    r = int(255 - (score * 2.55))
    g = int(score * 2.55)
    return [r, g, 0]

df["color"] = df["accountability_score"].apply(score_to_color)

# Sidebar filters
st.sidebar.header("🔍 Filter Properties")
zip_filter = st.sidebar.multiselect(
    "Zip Code", options=sorted(df["zip_code"].unique()), default=df["zip_code"].unique()
)
owner_filter = st.sidebar.text_input("Owner Name Contains")
score_min, score_max = st.sidebar.slider("Accountability Score Range", 0, 100, (0, 100))

filtered_df = df[
    (df["zip_code"].isin(zip_filter)) &
    (df["accountability_score"].between(score_min, score_max)) &
    (df["owner_name"].str.contains(owner_filter, case=False, na=False))
]

# Map
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
    tooltip={"text": "Owner: {owner_name}\\nScore: {accountability_score}"}
))

# Table
st.subheader("📋 Property Details")
st.dataframe(filtered_df[[
    "property_id", "address", "zip_code", "owner_name", "accountability_score"
]])
