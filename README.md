# AI Decision Intelligence Agent

A decision-intelligence prototype that goes beyond dashboards by automatically
detecting business risks and generating executive-level insights using
rule-based analytics and AI reasoning.

This project demonstrates how analytics pipelines can evolve from
**reporting → interpretation → decision guidance**.

---

## Problem

Traditional dashboards show metrics but do not help answer:

- What changed?
- Why did it change?
- What should we do next?

This system explores how **decision intelligence** can be layered on top of
analytics to automatically guide business actions.

---

## System Architecture

The project is intentionally divided into three layers:

### 1. Data Pipeline (ETL)
Processes business transaction data into structured analytics-ready datasets.

**Responsibilities**
- Data cleaning
- Feature creation
- Profit and margin calculations
- Weekly aggregation

---

### 2. Rules Engine (Signal Detection)
Detects business risks using deterministic logic.

Examples:
- Revenue decline detection
- Margin pressure detection
- Customer churn risk detection
- Regional underperformance detection

The rules engine outputs **structured business signals**, not explanations.

This ensures:
- transparency
- reliability
- explainability

---

### 3. AI Insight Generator (Interpretation Layer)
Consumes structured signals and produces:

- Executive summaries
- Risk interpretation
- Prioritized business issues
- Recommended actions

This layer turns analytics into **decision guidance**.

---

## Interface

A Streamlit dashboard presents:

- Business Health Snapshot
- Risk Signals
- Executive Insight
- Revenue and Margin Trends
- Data Explorer

The interface is intentionally calm and executive-focused.

---

## Demo Screenshots

Place screenshots inside an `assets/` folder in the repo.

---

## Tech Stack

- Python
- Pandas
- Streamlit
- Rule-based analytics
- AI insight generation logic
- Modular pipeline architecture

---

## How This Would Scale

In a production environment, this system could:

- Connect to a data warehouse
- Run on scheduled jobs (daily / weekly)
- Store insights centrally
- Trigger Slack / email alerts
- Add ML-based anomaly detection
- Integrate forecasting models

The current version focuses on **decision-intelligence architecture**, not infrastructure.

---

## Project Structure

src/
etl/
rules/
ai/
delivery/

data/
raw/
processed/

app.py
requirements.txt
README.md


---

## Note

This is a prototype designed to demonstrate
decision intelligence system design and analytics reasoning,
not a production SaaS application.
