import pandas as pd

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

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

negative_correlations = {
    var: correlation for var, correlation in correlations.items() if correlation < 0
}

if len(negative_correlations) > 0:
    print("Pasangan variabel independen dan dependen dengan korelasi negatif:")
    for var, correlation in negative_correlations.items():
        print(f"{dependent_var} - {var}: {correlation}")
else:
    print(
        "Tidak ada pasangan variabel independen dan dependen dengan korelasi negatif."
    )
