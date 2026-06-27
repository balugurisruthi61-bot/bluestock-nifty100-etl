-- 1
SELECT COUNT(*) FROM companies;

-- 2
SELECT COUNT(*) FROM balance_sheet;

-- 3
SELECT COUNT(*) FROM profitandloss;

-- 4
SELECT COUNT(*) FROM cashflow;

-- 5
SELECT * FROM companies LIMIT 5;

-- 6
SELECT company_id, COUNT(*) 
FROM balance_sheet
GROUP BY company_id;

-- 7
SELECT company_id, MAX(year)
FROM balance_sheet
GROUP BY company_id;

-- 8
SELECT company_id, MIN(year)
FROM balance_sheet
GROUP BY company_id;

-- 9
SELECT *
FROM profitandloss
ORDER BY net_profit DESC
LIMIT 5;

-- 10
SELECT *
FROM balance_sheet
WHERE total_assets > 10000;