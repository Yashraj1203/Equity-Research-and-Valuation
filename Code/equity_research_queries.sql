-- Equity Research analytics queries
-- Illustrative SQL patterns for a governed financial/market data warehouse.

-- Historical revenue and margin trend
SELECT fiscal_year,
       revenue,
       ebitda,
       ebitda / NULLIF(revenue,0) AS ebitda_margin,
       pat,
       pat / NULLIF(revenue,0) AS pat_margin
FROM company_financials
WHERE company = 'Eicher Motors'
ORDER BY fiscal_year;

-- Peer valuation snapshot
SELECT company, pe, ev_ebitda, roe
FROM peer_valuation_snapshot
WHERE sector = 'Automotive'
ORDER BY pe;

-- Scenario valuation inputs
SELECT scenario, revenue_growth, pat_margin, pe_multiple
FROM valuation_scenarios
ORDER BY scenario;

-- Earnings driver monitoring
SELECT period, royal_enfield_volume, vecv_volume, revenue, ebitda_margin
FROM operating_kpis
WHERE company = 'Eicher Motors'
ORDER BY period;
