import pandas as pd

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

# Menampilkan daftar kolom
print("Daftar kolom:")
print(df.columns)

# Menentukan tipe data kolom
numeric_columns = []
non_numeric_columns = []

for column in df.columns:
    if df[column].dtype in ["int64", "float64"]:
        numeric_columns.append(column)
    else:
        non_numeric_columns.append(column)

print("\nKolom numerik:")
print(numeric_columns)

print("\nKolom non-numerik:")
print(non_numeric_columns)
