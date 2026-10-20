
from pathlib import Path
import pandas as pd

source = Path("data/raw/clinical/PCOS_data_without_infertility.xlsx")
output = Path("data/processed/clinical_cleaned.csv")
target = "PCOS (Y/N)"

df = pd.read_excel(source, sheet_name="Full_new")

# Remove identifiers and the mostly empty unnamed column
df = df.drop(
    columns=["Sl. No", "Patient File No.", "Unnamed: 44"],
    errors="ignore",
)

# Convert invalid AMH values, such as 'a', to missing values
df["AMH(ng/mL)"] = pd.to_numeric(
    df["AMH(ng/mL)"], errors="coerce"
)

# Validate target labels
df[target] = pd.to_numeric(df[target], errors="raise")
if not set(df[target].dropna().unique()).issubset({0, 1}):
    raise ValueError("Unexpected PCOS target values.")

output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output, index=False)

print("Cleaning complete!")
print("Saved to:", output)
print("Cleaned shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum()[df.isna().sum() > 0].to_string())
print("\nTarget distribution:")
print(df[target].value_counts().sort_index().to_string())
