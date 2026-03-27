# ----------------------------------------
# Dataset Detective
# ----------------------------------------

import pandas as pd

# Load dataset (replace 'data.csv' with your file name)
file_path = "data.csv"
df = pd.read_csv(file_path)

print("=== Top 5 Rows ===")
print(df.head())

print("\n=== Dataset Info ===")
print(df.info())

# ------------------------------
# Find highest value column
# ------------------------------

# Select only numerical columns
numeric_columns = df.select_dtypes(include=['int64', 'float64'])

if not numeric_columns.empty:
    max_values = numeric_columns.max()
    highest_column = max_values.idxmax()
    highest_value = max_values.max()

    print("\n=== Highest Value in Dataset ===")
    print(f"Column with highest value: {highest_column}")
    print(f"Highest value: {highest_value}")
else:
    print("\nNo numerical columns found.")

# ------------------------------
# Count missing values
# ------------------------------

print("\n=== Missing Values Count ===")
print(df.isnull().sum())