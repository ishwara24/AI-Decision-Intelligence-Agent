from src.rules.business_rules import detect_business_signals


def generate_ai_insights():
    signals = detect_business_signals()

    if not signals:
        return "Business performance is stable with no significant risk signals detected."

    high = [s for s in signals if s["severity"] == "HIGH"]
    medium = [s for s in signals if s["severity"] == "MEDIUM"]

    lines = []

    # ---------------- HEADLINE ----------------
    if high:
        lines.append("⚠️ Overall Business Health: Needs Immediate Attention\n")
    else:
        lines.append("⚠️ Overall Business Health: Monitor Closely\n")

    # ---------------- INTERPRETATION ----------------
    lines.append("Key Observations:")

    for s in signals:
        if s["signal"] == "revenue_drop":
            lines.append(
                f"- Revenue declined {abs(s['change_pct'])}% in Week {s['week']} "
                f"compared to the {s['baseline']}, primarily driven by "
                f"{s['drivers']['product']} in the {s['drivers']['region']} region."
            )

        elif s["signal"] == "high_churn":
            lines.append(
                f"- {s['count']} transactions show high churn risk, "
                f"indicating potential customer retention issues."
            )

        elif s["signal"] == "low_margin":
            lines.append(
                f"- Average profit margin is {s['avg_margin']}%, "
                f"suggesting pricing or cost pressure."
            )

        elif s["signal"] == "regional_underperformance":
            lines.append(
                f"- The {s['region']} region is underperforming in total profit."
            )

    # ---------------- RECOMMENDATIONS ----------------
    lines.append("\nRecommended Actions:")

    if any(s["signal"] == "revenue_drop" for s in signals):
        lines.append("- Investigate product- and region-level demand drivers.")
    if any(s["signal"] == "high_churn" for s in signals):
        lines.append("- Launch targeted retention initiatives.")
    if any(s["signal"] == "low_margin" for s in signals):
        lines.append("- Review pricing and cost structures.")
    if any(s["signal"] == "regional_underperformance" for s in signals):
        lines.append("- Conduct regional performance audits.")

    return "\n".join(lines)
