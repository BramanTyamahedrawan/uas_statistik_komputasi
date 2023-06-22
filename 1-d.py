import pandas as pd
import numpy as np

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

holiday_week = df[df["Holiday_Flag"] == 1]["Weekly_Sales"]
non_holiday_week = df[df["Holiday_Flag"] == 0]["Weekly_Sales"]

# Menghitung varians
variance_holiday = np.var(holiday_week)
variance_non_holiday = np.var(non_holiday_week)

print("Varians Holiday Week:", variance_holiday)
print("Varians Non-Holiday Week:", variance_non_holiday)
