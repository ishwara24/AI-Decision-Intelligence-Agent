import os
from datetime import datetime
from src.ai.ai_insight_generator import generate_ai_insights


def generate_weekly_report():
    print("📤 Generating weekly business report...")

    insights = generate_ai_insights()

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Timestamped report name
    timestamp = datetime.now().strftime("%Y_%m_%d")
    report_path = f"reports/weekly_business_report_{timestamp}.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("WEEKLY BUSINESS INSIGHTS REPORT\n")
        file.write("=" * 40 + "\n\n")
        file.write(insights)

    print(f"✅ Report successfully saved at: {report_path}")


if __name__ == "__main__":
    generate_weekly_report()
