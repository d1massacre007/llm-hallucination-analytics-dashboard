import pandas as pd

# Load CSV
df = pd.read_csv(
    r'C:\Users\d1mas\Desktop\Python Codes\Project LLM\llm_hallucination_cleaned.csv'
)

# Remove notes column
df = df.drop(columns=["notes"])

# Convert created_date to datetime
df["created_date"] = pd.to_datetime(
    df["created_date"],
    errors="coerce"
)

# Show data types
print(df.dtypes)

# Basic EDA
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe(include="all"))