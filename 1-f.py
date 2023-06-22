import pandas as pd

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

store_max_cpi = df.groupby("Store")["CPI"].max()
store_with_max_cpi = store_max_cpi.idxmax()

print("Toko dengan nilai CPI tertinggi adalah toko ke ", store_with_max_cpi)
print("Nilai CPI tertinggi:", store_max_cpi[store_with_max_cpi])
