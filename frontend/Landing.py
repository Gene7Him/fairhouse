import streamlit as st

st.set_page_config(page_title="FairHouse | Housing Justice Platform", layout="centered")

#st.image("data/logo.png", width=160)

st.title("🏠 Welcome to FairHouse")

st.markdown("""
FairHouse is a civic technology platform built to expose housing injustice, track corporate landlord behavior, 
highlight risk zones, and give renters and communities the tools to fight back.

---

### 🚀 What You Can Do Here:

- 🗺️ Explore a live **map of properties** with accountability scores  
- 📊 See **ZIP code-level risk analysis**  
- 📣 Submit or read **tenant reports**  
- 📥 Download data for journalism or activism  
- 📡 Get alerts when new risks appear in your city  

---

### 💡 Why It Matters

Corporate and predatory ownership are pricing out working families, hiding behind shell companies,
and reshaping cities without consent. FairHouse puts the power back in people’s hands.

---

### 🔗 Ready to explore?

Use the sidebar to access:
- 🗺️ Map Explorer  
- 📊 Risk Analytics  
- 📣 Report Center  

or jump into the demo 👉 [here](Map_Explorer)
""")
