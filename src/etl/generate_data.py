import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)

# Number of records
NUM_RECORDS = 5000

# Date range
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(180)]

# Sample categories
regions = ["North", "South", "East", "West"]
products = ["Product_A", "Product_B", "Product_C", "Product_D"]
customer_segments = ["New", "Returning", "High Value"]

data = []

for i in range(NUM_RECORDS):
    date = random.choice(dates)
    product = random.choice(products)
    region = random.choice(regions)
    segment = random.choice(customer_segments)

    quantity = np.random.randint(1, 20)
    price = np.random.randint(200, 1500)
    revenue = quantity * price

    cost = revenue * np.random.uniform(0.55, 0.75)
    profit = revenue - cost

    churn_risk = np.random.choice(
        ["Low", "Medium", "High"],
        p=[0.6, 0.25, 0.15]
    )

    data.append([
        date.date(),
        product,
        region,
        segment,
        quantity,
        revenue,
        round(cost, 2),
        round(profit, 2),
        churn_risk
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "date",
        "product",
        "region",
        "customer_segment",
        "quantity",
        "revenue",
        "cost",
        "profit",
        "churn_risk"
    ]
)

# Save to CSV
output_path = "data/raw/business_data.csv"
df.to_csv(output_path, index=False)

print("✅ Synthetic business dataset generated successfully!")
print(f"📁 Saved at: {output_path}")
print(f"📊 Rows: {len(df)}")
