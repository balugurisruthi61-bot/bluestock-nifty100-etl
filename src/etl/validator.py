import pandas as pd

balance_df = pd.read_excel("data/Balancesheet.xlsx", header=1)
pnl_df = pd.read_excel("data/Profitandloss.xlsx", header=1)
cashflow_df = pd.read_excel("data/Cashflow.xlsx", header=1)
company_df = pd.read_excel("data/Companies.xlsx", header=1)

failures = []


def dq01_pk_unique(df):
    count = df["company_id"].duplicated().sum()

    if count > 0:
        failures.append({
            "rule":"DQ-01",
            "severity":"CRITICAL",
            "issue":"Duplicate company_id"
        })
def dq02_company_year(df):
    dup = df.duplicated(
        subset=["company_id","year"]
    ).sum()

    if dup > 0:
        failures.append({
            "rule":"DQ-02",
            "severity":"CRITICAL",
            "issue":"Duplicate company-year"
        })


def dq03_null_check(df):

    nulls = df.isnull().sum().sum()

    if nulls > 0:
        failures.append({
            "rule":"DQ-03",
            "severity":"WARNING",
            "issue":"Null values found"
        })


def dq04_positive_assets(df):

    if (df["total_assets"] <= 0).sum() > 0:
        failures.append({
            "rule":"DQ-04",
            "severity":"WARNING",
            "issue":"Invalid assets"
        })


if __name__ == "__main__":

    dq01_pk_unique(balance_df)

    dq02_company_year(balance_df)

    dq04_positive_assets(balance_df)

    print(pnl_df.columns)
    print(cashflow_df.columns)


    pd.DataFrame(failures).to_csv(
        "output/validation_failures.csv",
        index=False
    )


    print("Validation completed")

# DQ-05 Sales should be positive
def dq05_sales_check(df):
    if (df["sales"] <= 0).sum() > 0:
        failures.append({
            "rule":"DQ-05",
            "severity":"CRITICAL",
            "issue":"Invalid sales"
        })


# DQ-06 Net profit check
def dq06_profit_check(df):
    if df["net_profit"].isnull().sum() > 0:
        failures.append({
            "rule":"DQ-06",
            "severity":"WARNING",
            "issue":"Missing net profit"
        })


# DQ-07 EPS check
def dq07_eps_check(df):
    if df["eps"].isnull().sum() > 0:
        failures.append({
            "rule":"DQ-07",
            "severity":"WARNING",
            "issue":"Missing EPS"
        })


# DQ-08 OPM range check
def dq08_opm_check(df):
    invalid = (
        (df["opm_percentage"] < -100) |
        (df["opm_percentage"] > 100)
    ).sum()

    if invalid > 0:
        failures.append({
            "rule":"DQ-08",
            "severity":"WARNING",
            "issue":"Invalid OPM"
        })


# DQ-09 Cashflow check
def dq09_cashflow_check(df):
    if df["net_cash_flow"].isnull().sum() > 0:
        failures.append({
            "rule":"DQ-09",
            "severity":"WARNING",
            "issue":"Missing cash flow"
        })
        dq05_sales_check(pnl_df)
        dq06_profit_check(pnl_df)
        dq07_eps_check(pnl_df)
        dq08_opm_check(pnl_df)
        dq09_cashflow_check(cashflow_df)

# DQ-10 Dividend check
def dq10_dividend_check(df):
    if (df["dividend_payout"] < 0).sum() > 0:
        failures.append({
            "rule":"DQ-10",
            "severity":"WARNING",
            "issue":"Negative dividend"
        })


# DQ-11 Tax percentage check
def dq11_tax_check(df):
    invalid = (
        (df["tax_percentage"] < 0) |
        (df["tax_percentage"] > 100)
    ).sum()

    if invalid > 0:
        failures.append({
            "rule":"DQ-11",
            "severity":"WARNING",
            "issue":"Invalid tax percentage"
        })


# DQ-12 Company ID null check
def dq12_company_check(df):
    if df["company_id"].isnull().sum() > 0:
        failures.append({
            "rule":"DQ-12",
            "severity":"CRITICAL",
            "issue":"Missing company id"
        })


# DQ-13 Year null check
def dq13_year_check(df):
    if df["year"].isnull().sum() > 0:
        failures.append({
            "rule":"DQ-13",
            "severity":"WARNING",
            "issue":"Missing year"
        })


# DQ-14 Duplicate rows
def dq14_duplicate_check(df):
    if df.duplicated().sum() > 0:
        failures.append({
            "rule":"DQ-14",
            "severity":"WARNING",
            "issue":"Duplicate rows"
        })


# DQ-15 Cashflow validation
def dq15_cashflow_values(df):
    if df["net_cash_flow"].isnull().sum() > 0:
        failures.append({
            "rule":"DQ-15",
            "severity":"WARNING",
            "issue":"Missing cashflow"
        })


# DQ-16 Foreign key check
def dq16_fk_check():

    import sqlite3
    conn = sqlite3.connect("nifty100.db")

    result = conn.execute(
        "PRAGMA foreign_key_check"
    ).fetchall()

    if result:
        failures.append({
            "rule":"DQ-16",
            "severity":"CRITICAL",
            "issue":"Foreign key failure"
        })
        dq10_dividend_check(pnl_df)
        dq11_tax_check(pnl_df)
        dq12_company_check(balance_df)
        dq13_year_check(balance_df)
        dq14_duplicate_check(balance_df)
        dq15_cashflow_values(cashflow_df)
        dq16_fk_check()