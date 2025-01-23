import pandas as pd
import random

# Generate synthetic data
data = {
    "Machine_ID": range(1, 101),  # 100 machines
    "Temperature": [random.uniform(60, 100) for _ in range(100)],
    "Run_Time": [random.randint(50, 200) for _ in range(100)],
    "Downtime_Flag": [random.choice([0, 1]) for _ in range(100)],  # Binary flag
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("manufacturing_data.csv", index=False)

print("Synthetic dataset created: manufacturing_data.csv")
