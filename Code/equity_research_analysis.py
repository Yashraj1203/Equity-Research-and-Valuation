import pandas as pd
import numpy as np

hist = pd.read_csv("../Data/Eicher_Historical_Financials.csv")
peers = pd.read_csv("../Data/Eicher_Peer_Comparison.csv")

# Peer valuation statistics
ex_eicher = peers[peers["Company"] != "Eicher Motors"]
print("Peer median P/E:", ex_eicher["PE"].median())
print("Eicher P/E premium:", peers.loc[peers.Company=="Eicher Motors","PE"].iloc[0]/ex_eicher["PE"].median()-1)

# Historical growth
rev = hist.set_index("Metric").loc["Revenue (₹m)"]
print("FY22-FY26 revenue CAGR:", (rev["FY26"]/rev["FY22"])**(1/4)-1)

# Simple scenario engine
fy29_revenue = 23408 * 1.15 * 1.14 * 1.12
for name, growth, margin, multiple in [
    ("Bear", .08, .19, 24),
    ("Base", .12, .21, 30),
    ("Bull", .16, .225, 36)]:
    revenue = fy29_revenue/1.12*(1+growth)
    pat = revenue*margin
    print(name, "PAT:", round(pat,2), "Value/share:", round(pat*multiple/273,2))
