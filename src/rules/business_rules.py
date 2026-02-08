import pandas as pd

PROCESSED_DATA_PATH = "data/processed/processed_business_data.csv"


def detect_business_signals():
    """
    Returns structured business signals (NO narrative).
    """

    df = pd.read_csv(PROCESSED_DATA_PATH)
    signals = []

    # ---------------- Revenue Drop ----------------
    weekly_revenue = df.groupby("week")["revenue"].sum().sort_index()
    rolling_avg = weekly_revenue.rolling(window=4).mean()
    change_pct = (weekly_revenue - rolling_avg) / rolling_avg

    for week, change in change_pct.items():
        if pd.notna(change) and change < -0.15:
            week_data = df[df["week"] == week]

            product, region = (
                week_data
                .groupby(["product", "region"])["revenue"]
                .sum()
                .idxmax()
            )

            signals.append({
                "signal": "revenue_drop",
                "severity": "HIGH" if change < -0.25 else "MEDIUM",
                "week": int(week),
                "change_pct": round(change * 100, 1),
                "baseline": "4-week average",
                "drivers": {
                    "product": product,
                    "region": region
                }
            })

    # ---------------- Margin Pressure ----------------
    avg_margin = df["profit_margin"].mean()
    if avg_margin < 0.25:
        signals.append({
            "signal": "low_margin",
            "severity": "MEDIUM",
            "avg_margin": round(avg_margin * 100, 1)
        })

    # ---------------- Churn Risk ----------------
    churn_count = df[df["churn_risk"] == "High"].shape[0]
    if churn_count > 500:
        signals.append({
            "signal": "high_churn",
            "severity": "HIGH",
            "count": churn_count
        })

    # ---------------- Regional Underperformance ----------------
    region_profit = df.groupby("region")["profit"].sum()
    worst_region = region_profit.idxmin()

    signals.append({
        "signal": "regional_underperformance",
        "severity": "MEDIUM",
        "region": worst_region
    })

    return signals
