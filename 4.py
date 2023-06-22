import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

independent_var = "Fuel_Price"
dependent_var = "Weekly_Sales"
df["intercept"] = 1
X = df[["intercept", independent_var]]
y = df[dependent_var]
model = sm.OLS(y, X)

results = model.fit()
a = results.params["intercept"]
b = results.params[independent_var]

print("Variabel yang dihitung:")
print(f"Variabel independen: {independent_var}")
print(f"Variabel dependen: {dependent_var}")

print("\nHasil regresi:")
print(f"Koefisien a (intercept): {a:.2f}")
print(f"Koefisien b ({independent_var}): {b:.2f}")
print(f"Persamaan regresi: {dependent_var} = {a:.2f} + {b:.2f} * {independent_var}")
