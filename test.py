import pandas as pd
import statsmodels.api as sm

# Membaca file CSV
df = pd.read_csv("walmart.csv")

# Menentukan variabel independen dan dependen
independent_var = "Fuel_Price"
dependent_var = "Weekly_Sales"

# Menambahkan kolom konstan (intercept) ke dalam data
df["intercept"] = 1

# Menentukan data X (variabel independen) dan y (variabel dependen)
X = df[["intercept", independent_var]]
y = df[dependent_var]

# Membuat model regresi menggunakan Ordinary Least Squares (OLS)
model = sm.OLS(y, X)

# Melakukan fitting (penyesuaian) model ke data
results = model.fit()

# Mendapatkan hasil koefisien (a dan b) dari model regresi
a = results.params["intercept"]
b = results.params[independent_var]

# Menampilkan variabel yang dihitung
print("Variabel yang dihitung:")
print(f"Variabel independen: {independent_var}")
print(f"Variabel dependen: {dependent_var}")

# Menampilkan hasil regresi
print("\nHasil regresi:")
print(f"Koefisien a (intercept): {a:.2f}")
print(f"Koefisien b ({independent_var}): {b:.2f}")
print(f"Persamaan regresi: {dependent_var} = {a:.2f} + {b:.2f} * {independent_var}")
print("\nRingkasan Model:")
print(results.summary())
