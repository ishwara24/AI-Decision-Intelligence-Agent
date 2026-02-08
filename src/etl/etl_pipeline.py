import pandas as pd

# File paths
RAW_DATA_PATH = "data/raw/business_data.csv"
PROCESSED_DATA_PATH = "data/processed/processed_business_data.csv"

def run_etl():
    print("🔄 Starting ETL process...")

    # 1. Read raw data
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"📥 Raw data loaded: {df.shape}")

    # 2. Basic cleaning
    df.dropna(inplace=True)
    df["date"] = pd.to_datetime(df["date"])

    # 3. Feature engineering (KPIs)
    df["profit_margin"] = round(df["profit"] / df["revenue"], 2)
    df["week"] = df["date"].dt.isocalendar().week
    df["month"] = df["date"].dt.month

    # 4. Save processed data
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"✅ ETL complete. Processed data saved to {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    run_etl()
