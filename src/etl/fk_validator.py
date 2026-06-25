import pandas as pd

companies = pd.read_excel("data/companies.xlsx", header=1)
balancesheet = pd.read_excel("data/balancesheet.xlsx", header=1)

valid_ids = set(companies["id"])

invalid_rows = balancesheet[
    ~balancesheet["company_id"].isin(valid_ids)
]

print("Invalid FK Records:", len(invalid_rows))

if len(invalid_rows) > 0:
    print(invalid_rows[["company_id"]].head())

#print(companies[companies["company_name"].str.contains("Zydus", case=False, na=False)])