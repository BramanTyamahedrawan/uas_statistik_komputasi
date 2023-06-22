import pandas as pd
import numpy as np

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

df_store_4 = df[df["Store"] == 4]
columns = ["Fuel_Price", "CPI", "Unemployment"]

# Menghitung kuartil
quartiles = {}
for column in columns:
    quartiles[column] = {
        "Q1": np.percentile(df_store_4[column], 25),
        "Q2": np.percentile(df_store_4[column], 50),
        "Q3": np.percentile(df_store_4[column], 75),
        "IQR": np.percentile(df_store_4[column], 75)
        - np.percentile(df_store_4[column], 25),
    }

for column, stats in quartiles.items():
    print("Kolom:", column)
    print("Q1:", stats["Q1"])
    print("Q2 (Median):", stats["Q2"])
    print("Q3:", stats["Q3"])
    print("IQR:", stats["IQR"])
    print()
