# Institutional Equity Research & Financial Valuation Model


> An end-to-end equity research, valuation, and financial modeling case study for **Eicher Motors Limited (NSE: EICHERMOT)** — covering Royal Enfield and VE Commercial Vehicles (VECV).

---

## 📌 Project Overview

The project demonstrates an investment analyst's complete workflow: transforming public regulatory and financial disclosures into normalized financial statements, a programmatic valuation model, a 2-stage Discounted Cash Flow (DCF) engine built to J.P. Morgan research standards, trading comps benchmarking, and scenario sensitivity analysis.

```
Company Research & Public Disclosures (Annual Reports, NSE, SIAM)
    ↓
Financial Statement Normalization (FY22–FY26 Reported Actuals)
    ↓
Operational KPI & Volume Analysis (Royal Enfield & VECV Commercial Vehicles)
    ↓
Analyst Forecasting Engine (FY27E–FY29E Operating Levers)
    ↓
Dual-Pillar Valuation Architecture
    ├── 1. J.P. Morgan Multi-Stage DCF Model (NOPAT, UFCF Schedule, WACC Sensitivity)
    └── 2. Relative Valuation Comps (Automotive OEM Peer Multiples: P/E, EV/EBITDA, ROE)
    ↓
Scenario Analysis (Bear / Base / Bull Sensitivity Matrix)
    ↓
Automated Real-Time Audit Controls & Governance
    ↓
Investment Thesis & Catalysts / Monitorables
```

---

## 🎯 Business & Research Objective

**Core Research Question:** Can Eicher Motors sustain sufficient volume growth, margin expansion, and international traction to justify its valuation premium over broader domestic auto OEM peers?

- **Volume & Brand Momentum** — Track Royal Enfield's scale expansion across premium middleweight motorcycles (250cc–750cc) and examine commercial vehicle cycle dynamics at VECV.
- **Operating Leverage** — Model historical operating margin stability (>24.5%) and evaluate pass-through of commodity deflation vs. marketing investment.
- **Intrinsic vs. Relative Value** — Contrast intrinsic cash-flow value derived from an explicit multi-stage DCF against market-implied trading multiples.
- **Downside Risk Protection** — Stress-test valuation across Bear, Base, and Bull cases using exit P/E multiples and operating margin assumptions.

---

## 🗃️ Dataset & Financial Boundary

| Category | Description |
|---|---|
| **Audited Financials (FY22–FY26)** | Revenue, EBITDA, PAT, and cash balance normalized from audited annual reports and the NSE financial disclosure dated 22 May 2026 |
| **Operating KPIs** | Monthly volume dispatches for Royal Enfield and commercial vehicle sales for VECV |
| **Capital Structure** | Diluted share count of 27.30 crore equity shares; net cash/liquid investments proxy of ₹5,450 crore |
| **Peer Valuation Snapshot** | Comparable multiples (P/E, EV/EBITDA, ROE) for Bajaj Auto, Maruti Suzuki, Mahindra & Mahindra, TVS Motor, and Hyundai Motor India, as of 24 September 2026 |

> **Data Boundary Note:** Historical figures (FY22–FY26) represent reported facts from public company disclosures. Projections (FY27E–FY29E), WACC, terminal growth, and scenario exit multiples represent analyst-built assumptions.

---

## 🏗️ Financial Model Architecture

The institutional model — `Equity_Research_Valuation_Model_Institutional.xlsx` — is structured into five integrated, formula-driven worksheets:

### 1. `00_Executive_Summary`
- Executive KPI summary cards (Reference Price, Target Price, Implied DCF, FY26 PAT)
- Valuation synthesis table summarizing Base, Bull, Bear, DCF, and Peer Median targets alongside implied upside/downside

### 2. `01_Financials`
- Continuous 8-year operational schedule: historical actuals (FY22–FY26) and 3-year explicit forecasts (FY27E–FY29E)
- Dynamic line modeling: Revenue YoY growth, EBITDA and EBITDA margin, PAT and PAT margin, Royal Enfield dispatch volumes, VECV vehicle volumes

### 3. `02_Scenario_Analysis`
- 3-tier scenario engine evaluating Bear, Base, and Bull operational cases
- Dynamically derives FY29E Revenue, PAT, Equity Value, and Target Share Price based on selected exit P/E multiples (24.0x / 30.0x / 36.0x)

### 4. `03_DCF_Model` (J.P. Morgan Research Standard)
- Multi-stage horizon: historical track record (FY22–FY26), explicit forecast (FY27E–FY29E), outside-in extrapolation (FY30E–FY32E), and terminal year (TV)
- Granular Unlevered Free Cash Flow (UFCF/FCFF) build from NOPAT (EBIT − 25.17% effective tax), D&A addback, capex intensity, and working capital investment
- Valuation bridge: Enterprise Value → Equity Value, with explicit cash-flow PV vs. Terminal Value contribution
- 5×5 2D sensitivity matrix: implied share price across WACC (9.5%–11.5%) and perpetual growth (g = 4.0%–6.0%)

### 5. `04_Assumptions_Audit`
- Central parameter registry: WACC (10.5%), terminal growth (g = 5.0%), D&A run-rate (1.8%), capex ratio (4.5%), NWC investment (2.5%)
- Automotive peer comp benchmarking table
- Automated real-time error controls and validation checks

---

## 📊 Valuation Summary & Findings

| Valuation Framework | Target Price / Share | Implied Upside / (Downside) | Key Assumptions / Multiples | Model Reference |
|---|---|---|---|---|
| **Base Case (P/E)** | ₹7,931.64 | +8.0% | FY29E PAT Margin 21.0% \| Exit P/E 30.0x | `02_Scenario_Analysis` |
| **Bull Case (P/E)** | ₹10,562.03 | +43.8% | FY29E PAT Margin 22.5% \| Exit P/E 36.0x | `02_Scenario_Analysis` |
| **Bear Case (P/E)** | ₹5,535.96 | −24.6% | FY29E PAT Margin 19.0% \| Exit P/E 24.0x | `02_Scenario_Analysis` |
| **J.P. Morgan DCF (Perpetuity)** | ₹4,400 – ₹4,850 | Sensitivity-bound | WACC 10.5% \| Perpetual Growth (g) 5.0% | `03_DCF_Model` |
| **Automotive Peer Median Comps** | ₹5,045.96 | −31.3% | Peer Median P/E 24.98x (parity cross-check) | `04_Assumptions_Audit` |

**Current Market Reference Share Price:** ₹7,344.00 (NSE reference date: September 2026)

---

## 🧮 Analytical SQL & Governed Analytics

`Code/equity_research_queries.sql` illustrates analytical queries for a governed financial data warehouse:

- **Historical Trend Query** — Calculates annual Revenue, EBITDA, PAT, and margin trajectories using `NULLIF()` guards
- **Peer Valuation Snapshot** — Ranks automotive peers by valuation multiples (P/E, EV/EBITDA, ROE)
- **Scenario Driver Ingestion** — Structures scenario levers for programmatic model execution
- **Volume & Operational KPI Tracking** — Tracks Royal Enfield dispatch volumes and VECV sales alongside financial performance

---

## ✅ Model Controls & Integrity Audit

Dynamic verification formulas on `04_Assumptions_Audit` include:

- **DCF Denominator Stability** — Confirms WACC > terminal growth (g) to prevent a negative denominator
- **Terminal Value Share %** — Flags if Terminal Value represents >85% of Total Enterprise Value
- **Scenario Monotonicity** — Verifies Bear Target < Base Target < Bull Target
- **Dashboard Synchronization** — Verifies Executive Summary cards match internal calculations on the DCF and Scenario sheets in real time

---

## ⚠️ Investment Risks & Monitorables

### Primary Risks
- **Valuation Compression** — Eicher trades at ~36.4x trailing earnings vs. a 25.0x peer median; shifts in macro rates or volume misses could compress multiples
- **Competitive Ingress** — OEM competition targeting the middleweight motorcycle segment (350cc–650cc) could pressure pricing power and volume run-rates
- **Commercial Vehicle Cyclicality** — VECV performance remains tied to cyclical Indian infrastructure, freight, and fleet replacement demand

### Catalysts & Quarterly Monitorables
- Monthly Royal Enfield domestic dispatches and export volume mix
- EBITDA margin resilience amid raw material price fluctuations
- New product cadence, motorcycle platform launches, and global network expansion
- Growth and profitability updates regarding VECV and Volvo Group financial services initiatives

---

## 📁 Repository Structure

```
Equity_Research_Investment_Thesis_Eicher_Motors/
│
├── README.md                                              # Master project overview & investment thesis
│
├── Model/
│   └── Equity_Research_Valuation_Model.xlsx                
│
├── Data/
│   ├── Eicher_Historical_Financials.csv                    # Audited FY22–FY26 reported results
│   ├── Eicher_Peer_Comparison.csv                          # Automotive OEM peer valuation data
│   └── Eicher_Scenario_Valuation.csv                       # Operating scenario inputs
│
├── Code/                                  
│   ├── equity_research_analysis.py                         
│   └── equity_research_queries.sql                         
│
└── Docs/
    ├── Methodology.md                               
    └── Source.md                                    
```

---



# Run the CAGR & scenario analysis script
python Code/equity_research_analysis.py
```

Open `Model/Equity_Research_Valuation_Model.xlsx` to explore the full 5-tab valuation model, or query `Code/equity_research_queries.sql` against the CSV datasets in `Data/` using your preferred SQL engine.

---

## 🛠️ Skills Demonstrated

- Financial Statement Analysis & Normalization
- 2-Stage Discounted Cash Flow (DCF) Modeling
- J.P. Morgan Research Standards & UFCF Schedule Construction
- 2D Sensitivity Table Construction (WACC vs. g)
- Trading Comps Benchmarking (P/E, EV/EBITDA, ROE)
- Scenario & Sensitivity Analysis (Bear / Base / Bull)
- Programmatic Excel Modeling (openpyxl, dynamic linking, color coding)
- Analytical SQL (`NULLIF`, aggregations, window functions)
- Python Financial Analysis (pandas, numpy)
- SEBI Research Analyst Regulatory Framing

---

## 📚 Sources

- Eicher Motors Investor Disclosures & Annual Reports (FY22–FY26)
- Eicher Motors Audited Results / Press Release (NSE-hosted disclosure dated 22 May 2026)
- SEBI (Research Analysts) Regulations Framework
- Automotive Peer Reference Market Ratios (StockAnalysis, accessed September 2026)

---

## ⚖️ Analytical Boundaries & Disclaimer

This repository is an **equity research modeling case study only**. It does **not** provide:

- Registered investment advice, buy/sell solicitations, or financial recommendations
- Guarantees of future stock price performance or operating outcomes
- Non-public insider information or company guidance

Historical figures reflect published public information. Projections are forward-looking analyst estimates subject to market and operational uncertainty.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Developed by [Yashraj1203](https://github.com/Yashraj1203)*
