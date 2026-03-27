# ----------------------------------------
# Data Doctor - Dataset Cleaning
# ----------------------------------------

import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("=== Original Dataset ===")
print(df.head())

# -----------------------------
# 1. Handle Missing Values
# -----------------------------
# Fill missing numeric values with column mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing text values with "Unknown"
df.fillna("Unknown", inplace=True)

# -----------------------------
# 2. Remove Duplicate Rows
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# 3. Standardize Text Columns
# -----------------------------
# Convert all text columns to lowercase and remove spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().str.lower()

print("\n=== Cleaned Dataset ===")
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nDataset cleaned and saved as 'cleaned_data.csv'")