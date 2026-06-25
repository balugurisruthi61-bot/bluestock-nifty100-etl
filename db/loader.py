import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

companies = pd.read_excel("data/companies.xlsx", header=1)

companies.to_sql(
    "companies",
    conn,
    if_exists="append",
    index=False
)

print("Companies loaded:", len(companies))

conn.close()