import pandas as pd

# Load raw clinic administration data
df = pd.read_csv("data/raw/clinic_admin_records.csv")

# Basic overview
print("Dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

# Status overview
status_summary = df["status"].value_counts()
print("\nStatus summary:")
print(status_summary)

# Find records needing attention
issues = df[df["status"].isin(["Missing", "Duplicate", "Pending"])]

print("\nRecords needing attention:")
print(issues)

# Export cleaned/filtered issue report
issues.to_csv("data/cleaned/clinic_records_needing_attention.csv", index=False)

print("\nIssue report exported successfully.")
