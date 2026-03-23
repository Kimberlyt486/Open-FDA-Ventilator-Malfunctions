# Vent-Guardian-API: Medical Device Vigilance Pipeline

## 📊 Overview
VentGuard is an end-to-end data pipeline that automates the collection and analysis of ventilator malfunctions. Using the **openFDA API**, this project monitors real-world ventilator performance data, providing a Post-Market Surveillance dashboard for clinical engineering and compliance teams.

As a **Registered Respiratory Therapist (RRT)** transitioning into Software Engineering, I built this tool to bridge the gap between bedside clinical observations and data-driven safety analytics.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas (ETL & Data Munging), Requests (API Interaction)
* **Data Source:** openFDA Medical Device Adverse Event (MAUDE) API
* **Storage:** CSV / SQL-ready Dataframes

## 🚀 Key Features & Engineering Challenges

### 1. Advanced API Integration
* Implemented a dynamic query system to filter 1M+ FDA records for specific generic terms (e.g., "ventilator") and event types ("malfunction").
* Integrated **API Key Authentication** and error-handling for 403 (Forbidden) and 400 (Bad Request) status codes.