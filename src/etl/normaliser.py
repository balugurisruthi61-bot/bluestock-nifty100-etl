import pandas as pd

def normalize_year(year):
    if pd.isna(year):
        return None

    return str(year).strip()[-4:]

def normalize_ticker(ticker):
    if pd.isna(ticker):
        return None

    return str(ticker).strip().upper()