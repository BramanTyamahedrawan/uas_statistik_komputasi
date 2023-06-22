import pandas as pd

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

store_avg_sales = df.groupby("Store")["Weekly_Sales"].mean()
average_same = store_avg_sales.nunique() == 1

if average_same:
    print("Rata-rata weekly sales sama di setiap toko")
else:
    print("Rata-rata weekly sales berbeda di setiap toko")
    print("Nilai rata-rata weekly sales untuk setiap toko:")
    for store, avg_sales in store_avg_sales.items():
        print("Toko", store, ":", avg_sales)
