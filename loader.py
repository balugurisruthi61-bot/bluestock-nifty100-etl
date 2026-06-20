import pandas as pd

def normalize_year(year):
    return str(year)[-4:]

def normalize_ticker(ticker):
    return str(ticker).strip().upper()

df = pd.read_excel("data/balancesheet.xlsx", header=1)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

df["year"] = df["year"].apply(normalize_year)
df["company_id"] = df["company_id"].apply(normalize_ticker)

print(df[["company_id", "year"]].head())