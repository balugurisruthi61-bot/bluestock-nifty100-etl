 PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    company_name TEXT,
    website TEXT,
    face_value REAL,
    book_value REAL,
    roce_percentage REAL,
    roe_percentage REAL
);


CREATE TABLE IF NOT EXISTS balance_sheet (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year INTEGER,
    equity_capital REAL,
    reserves REAL,
    borrowings REAL,
    total_liabilities REAL,
    total_assets REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS profitandloss (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year INTEGER,
    sales REAL,
    expenses REAL,
    operating_profit REAL,
    net_profit REAL,
    eps REAL,
    dividend_payout REAL,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS cashflow (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year INTEGER,
    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL,
    net_cash_flow REAL,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    document TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS prosandcons (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    pros TEXT,
    cons TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT
);


CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    price REAL,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);


CREATE TABLE IF NOT EXISTS financial_ratios (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    ratio_name TEXT,
    ratio_value REAL,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);