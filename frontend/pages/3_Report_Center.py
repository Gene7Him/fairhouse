import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("📣 Report Center")

df = pd.read_csv("../data/raw/sample_properties_geocoded.csv")

st.subheader("📥 Submit a Report")

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

st.subheader("📄 Recent Reports")
if os.path.exists("data/reports.csv"):
    st.dataframe(pd.read_csv("data/reports.csv").sort_values("timestamp", ascending=False))
else:
    st.info("No reports yet.")
