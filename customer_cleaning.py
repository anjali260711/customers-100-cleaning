import pandas as pd

# Step 1: Load Data
df = pd.read_csv("customers-100.csv")
print("Initial Shape:", df.shape)

# Step 2: Deduplication
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

# Step 3: Column Management
if "Index" in df.columns:
    df.drop(columns=["Index"], inplace=True)
df.rename(columns={"Phone 1":"Phone"}, inplace=True)

# Step 4: Missing Value Handling
print("Missing values:\n", df.isna().sum())
df.dropna(subset=["Customer Id"], inplace=True)

# Step 5: Data Type Correction
df["Phone"] = df["Phone"].astype(str)

# Step 6: Format Standardization
df["City"] = df["City"].str.strip().str.title()
df["Country"] = df["Country"].str.strip().str.title()

# Step 7: Validation
assert df.duplicated().sum() == 0
assert df["Customer Id"].isna().sum() == 0

# Step 8: Save Cleaned File
df.to_csv("cleaned_customers.csv", index=False)
print("✅ Cleaned dataset saved as cleaned_customers.csv")




