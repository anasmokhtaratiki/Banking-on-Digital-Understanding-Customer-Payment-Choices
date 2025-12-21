# ETL Process – Digital Payment Adoption in Tunisia
# This script documents the Extract, Transform, and Load (ETL) process
# applied to the raw dataset used in the Business Intelligence project.
# The objective is to clean, transform, and prepare customer transaction
# data for analyzing digital payment adoption.

import pandas as pd

# Load the raw dataset
df_raw = pd.read_excel("BankChurners_clean_raw.xlsx")

print("Raw dataset loaded successfully")
print(df_raw.head())

# Select relevant columns for the analysis
columns_to_keep = [
    "customer_id",
    "activity_status",
    "age",
    "gender",
    "dependents",
    "education_level",
    "marital_status",
    "income_category",
    "card_category",
    "customer_tenure_months",
    "transaction_count",
    "transaction_amount"
]

df = df_raw[columns_to_keep]

# Standardize education level values
df["education_level"] = df["education_level"].replace(
    ["Post-Graduate", "Doctorate", "College"],
    "Graduate"
)

# Check for duplicate customer identifiers
duplicate_count = df.duplicated(subset=["customer_id"]).sum()
print("Duplicate customer_id count:", duplicate_count)

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Display data types
print("Data types:")
print(df.dtypes)

# Save the cleaned dataset
df.to_csv("digital_payment_usage_clean.csv", index=False)
print("Cleaned dataset saved successfully")
