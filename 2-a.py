import pandas as pd
from scipy.stats import kstest, norm

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

weekly_sales = df["Weekly_Sales"]
fuel_price = df["Fuel_Price"]
statistic_ws, p_value_ws = kstest(weekly_sales, "norm")
statistic_fp, p_value_fp = kstest(fuel_price, "norm")

alpha = 0.05

print("Uji Normalitas Kolom 'Weekly_Sales':")
print("Nilai statistik:", statistic_ws)
print("Nilai p-value:", p_value_ws)

if p_value_ws < alpha:
    print(
        "Berdasarkan uji KS, kolom 'Weekly_Sales' tidak berasal dari distribusi normal"
    )
else:
    print("Berdasarkan uji KS, kolom 'Weekly_Sales' berasal dari distribusi normal")

print()

print("Uji Normalitas Kolom 'Fuel_Price':")
print("Nilai statistik:", statistic_fp)
print("Nilai p-value:", p_value_fp)

if p_value_fp < alpha:
    print("Berdasarkan uji KS, kolom 'Fuel_Price' tidak berasal dari distribusi normal")
else:
    print("Berdasarkan uji KS, kolom 'Fuel_Price' berasal dari distribusi normal")
