import sqlite3
import pandas as pd
import os


conn = sqlite3.connect("nifty100.db")

conn.execute("PRAGMA foreign_keys = ON")


files = {
    "companies": "data/companies.xlsx",
    "balance_sheet": "data/balancesheet.xlsx",
    "profitandloss": "data/profitandloss.xlsx",
    "cashflow": "data/cashflow.xlsx",
    "analysis": "data/analysis.xlsx",
    "documents": "data/documents.xlsx",
    "prosandcons": "data/prosandcons.xlsx"
}


audit = []


for table, file in files.items():

    df = pd.read_excel(file, header=1)

    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )

    audit.append({
        "table": table,
        "rows_loaded": len(df),
        "file": file
    })


pd.DataFrame(audit).to_csv(
    "output/load_audit.csv",
    index=False
)


print("Full Data Load Completed")

conn.close()