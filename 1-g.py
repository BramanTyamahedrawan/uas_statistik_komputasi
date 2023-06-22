import pandas as pd

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

mean_cpi_holiday = df[df["Holiday_Flag"] == 1]["CPI"].mean()
mean_cpi_non_holiday = df[df["Holiday_Flag"] == 0]["CPI"].mean()

if mean_cpi_holiday > mean_cpi_non_holiday:
    print("Rata-rata CPI lebih tinggi pada holiday week")
    print("Rata-rata CPI holiday week:", mean_cpi_holiday)
    print("Rata-rata CPI non-holiday week:", mean_cpi_non_holiday)
elif mean_cpi_holiday < mean_cpi_non_holiday:
    print("Rata-rata CPI lebih tinggi pada non-holiday week")
    print("Rata-rata CPI holiday week:", mean_cpi_holiday)
    print("Rata-rata CPI non-holiday week:", mean_cpi_non_holiday)
else:
    print("Rata-rata CPI sama pada holiday week dan non-holiday week")
    print("Rata-rata CPI:", mean_cpi_holiday)
