import pandas as pd

df = pd.read_csv("walmart.csv")

independent_vars = [
    "Store",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment",
    "Holiday_Flag",
]
correlations = {}
dependent_var = "Weekly_Sales"

for var in independent_vars:
    correlation = df[var].corr(df[dependent_var])
    correlations[var] = correlation

for var, correlation in correlations.items():
    print(f"Korelasi antara {dependent_var} - {var}: {correlation}")
