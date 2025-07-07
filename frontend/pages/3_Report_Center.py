import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

st.title("📣 Report Center")

# Connect to Neon DB using Streamlit secrets
engine = create_engine(st.secrets["DATABASE_URL"])

# Load properties for dropdown
df = pd.read_sql("SELECT property_id, address FROM properties ORDER BY property_id", engine)

st.subheader("📥 Submit a Report")

with st.form("report_form"):
    selected_id = st.selectbox(
        "Select Property",
        df.apply(lambda row: f"{row['property_id']} — {row['address']}", axis=1)
    )
    issue_type = st.selectbox("Issue Type", ["Rent Hike", "Unsafe Conditions", "Eviction Threat", "Harassment", "Other"])
    description = st.text_area("Describe the issue")
    reporter_name = st.text_input("Your Name (optional)")
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        property_id = selected_id.split(" — ")[0]
        with engine.connect() as conn:
            insert_query = text("""
                INSERT INTO reports (timestamp, property_id, issue_type, description, reporter_name)
                VALUES (:timestamp, :property_id, :issue_type, :description, :reporter_name)
            """)
            conn.execute(insert_query, {
                "timestamp": datetime.utcnow().isoformat(),
                "property_id": property_id,
                "issue_type": issue_type,
                "description": description,
                "reporter_name": reporter_name or "Anonymous"
            })
            conn.commit()
        st.success("✅ Report submitted successfully.")

st.subheader("📄 Recent Reports")
recent_reports = pd.read_sql("""
    SELECT r.timestamp, p.address, r.issue_type, r.description, r.reporter_name
    FROM reports r
    JOIN properties p ON r.property_id = p.property_id
    ORDER BY r.timestamp DESC
    LIMIT 50
""", engine)
st.dataframe(recent_reports)
