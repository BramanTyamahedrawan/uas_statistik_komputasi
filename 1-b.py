import pandas as pd
import numpy as np

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

df_store_4 = df[df["Store"] == 4]
numeric_columns = []
for column in df_store_4.columns:
    if df_store_4[column].dtype in ["int64", "float64"]:
        numeric_columns.append(column)

# Menghitung statistik deskriptif
descriptive_stats = {}
for column in numeric_columns:
    descriptive_stats[column] = {
        "mean": np.mean(df_store_4[column]),
        "median": np.median(df_store_4[column]),
        "simpangan_baku": np.std(df_store_4[column]),
        "variance": np.var(df_store_4[column]),
    }

for column, stats in descriptive_stats.items():
    print("Kolom:", column)
    print("Mean:", stats["mean"])
    print("Median:", stats["median"])
    print("Simpangan Baku:", stats["simpangan_baku"])
    print("Variance:", stats["variance"])
    print()
