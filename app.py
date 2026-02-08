import streamlit as st
import pandas as pd
from datetime import datetime
from typing import List

from src.rules.business_rules import detect_business_signals
from src.ai.ai_insight_generator import generate_ai_insights
# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Business Decision Intelligence",
    layout="wide"
)

# --------------------------------------------------
# REQUIRED SCHEMA
# --------------------------------------------------
def validate_schema(df: pd.DataFrame) -> List[str]:
    return list(REQUIRED_COLUMNS - set(df.columns))
REQUIRED_COLUMNS = {
    "date",
    "product",
    "region",
    "customer_segment",
    "quantity",
    "revenue",
    "cost",
    "profit",
    "profit_margin",
    "week",
    "month",
    "churn_risk",
}

# --------------------------------------------------
# DATA LOADING
# --------------------------------------------------
def load_default_data():
    return pd.read_csv("data/processed/processed_business_data.csv")


def load_uploaded_data(file):
    return pd.read_csv(file)



# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("## Business Decision Intelligence Report")
st.markdown(
    f"<span style='color:gray'>Automated performance analysis • "
    f"Last updated: {datetime.now().strftime('%d %b %Y, %H:%M')}</span>",
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# CSV UPLOAD (OPTION B)
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload business data (CSV)",
    type=["csv"],
    help="Upload a CSV with the required business metrics"
)

# ---------------- UX GUARD ----------------
if not uploaded_file:
    st.info(
        "Please upload a CSV file to generate a decision intelligence report.\n\n"
        "The file must follow the expected schema (date, revenue, profit, churn, etc.)."
    )
    st.stop()

# ---------------- LOAD RAW DATA ----------------
df = load_uploaded_data(uploaded_file)

# ---------------- VALIDATE SCHEMA FIRST ----------------
missing_cols = validate_schema(df)

if missing_cols:
    st.error(
        f"Uploaded file is missing required columns: {', '.join(missing_cols)}"
    )
    st.stop()

# ---------------- SAFE TRANSFORMATIONS ----------------
df["date"] = pd.to_datetime(df["date"])

is_compatible_schema = True



# --------------------------------------------------
# BUSINESS HEALTH SNAPSHOT
# --------------------------------------------------
st.markdown("### Business Health Snapshot")

col_left, col_right = st.columns([1, 2])

recent_margin = df.sort_values("date").tail(50)["profit_margin"].mean()

# Health is derived ONLY from signals (single source of truth)
if is_compatible_schema:
    signals = detect_business_signals()


    if any(s["severity"] == "HIGH" for s in signals):
        health_status = "Needs Attention"
    elif any(s["severity"] == "MEDIUM" for s in signals):
        health_status = "Monitor"
    else:
        health_status = "Stable"
else:
    health_status = "Informational"


with col_left:
    if health_status == "Needs Attention":
        st.markdown("#### 🔴 Needs Attention")
        st.caption("High-severity risks detected despite healthy margins")
    elif health_status == "Monitor":
        st.markdown("#### 🟠 Monitor Closely")
        st.caption("Moderate risks detected — watch trends")
    elif health_status == "Stable":
        st.markdown("#### 🟢 Stable")
        st.caption("No significant risk signals detected")
    else:
        st.markdown("#### ℹ️ Informational")
        st.caption("Risk evaluation disabled for uploaded data")

    st.markdown(
        f"- Avg profit margin (recent): **{round(recent_margin * 100, 1)}%**"
    )

with col_right:
    st.markdown("**Revenue Trend**")
    revenue_trend = df.groupby("week")["revenue"].sum()
    st.line_chart(revenue_trend, height=180)

    st.markdown("**Profit Margin Trend**")
    margin_trend = df.groupby("week")["profit_margin"].mean()
    st.line_chart(margin_trend, height=180)

st.divider()

# --------------------------------------------------
# KEY BUSINESS SIGNALS
# --------------------------------------------------
st.markdown("### Key Business Signals")

if not is_compatible_schema:
    st.info("Rule-based risk detection is unavailable for this dataset.")
else:
    signals = detect_business_signals()



    if signals:
        for s in signals:
            icon = "🔴" if s["severity"] == "HIGH" else "🟠"

            if s["signal"] == "revenue_drop":
             st.markdown(
            f"{icon} Revenue dropped {abs(s['change_pct'])}% in week {s['week']} "
            f"(vs {s['baseline']})."
        )

            elif s["signal"] == "high_churn":
             st.markdown(
            f"{icon} {s['count']} transactions show high churn risk."
        )

            elif s["signal"] == "low_margin":
             st.markdown(
            f"{icon} Average profit margin is {s['avg_margin']}%."
        )

            elif s["signal"] == "regional_underperformance":
             st.markdown(
            f"{icon} {s['region']} region is underperforming in total profit."
        )


st.divider()

# --------------------------------------------------
# EXECUTIVE INSIGHT
# --------------------------------------------------
st.markdown("### Executive Insight")

if not is_compatible_schema:
    st.info("AI-generated executive insights are unavailable for this dataset.")
else:
    insight_text = generate_ai_insights()


    st.markdown(
        f"""
        <div style="padding:12px; border-left:4px solid #999;">
        {insight_text.replace("\n", "<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# --------------------------------------------------
# RECOMMENDED ACTIONS
# --------------------------------------------------
st.markdown("### Recommended Actions")

st.markdown(
    """
    - Investigate sharp revenue declines and identify demand drivers  
    - Review pricing and cost structures for margin improvement  
    - Launch retention programs for high churn-risk segments  
    - Conduct regional performance audits to address profitability gaps  
    """
)

# --------------------------------------------------
# DATA EXPLORER (SECONDARY)
# --------------------------------------------------
with st.expander("View underlying data"):
    st.dataframe(df, use_container_width=True)

