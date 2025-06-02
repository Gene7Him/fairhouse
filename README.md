# 🏡 FairHouse: Housing Justice Platform

FairHouse is a full-stack system for exposing housing injustice, scoring landlord behavior, and empowering communities to act. It ingests housing data, analyzes ownership patterns, and lets users report abuse — all while serving insights through APIs and dashboards.

I built FairHouse to expose the systemic abuse in housing and give power back to the people. It’s used by real renters, activists, and journalists to track injustice, organize, and vote out politicians protecting predatory landlords. This is the kind of system I want to keep building — tools that make the world more just, at scale.

## 🚀 Features
- Ingests housing/property/ownership data from public sources
- Computes landlord "accountability scores"
- Visualizes housing risk zones by zip code
- API for developers, activists, and journalists
- Streamlit dashboard (MVP)
- Modular backend for scaling up

## 🧰 Tech Stack
- Python + FastAPI (backend)
- PostgreSQL (relational DB)
- Streamlit (frontend MVP)
- Docker (for deployment)
- Airflow-ready ETL pipeline

## 📁 Project Structure
(see repo folders)

## 🚧 Roadmap
- [x] Set up backend + basic data ingestion
- [ ] Add accountability score logic
- [ ] Deploy dashboard with map + filters
- [ ] Add alerts and reporting features

## 🛠️ Getting Started

```bash
git clone https://github.com/Gene7Him/fairhouse.git
cd fairhouse
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.api.main:app --reload
```

## 📜 License
MIT
