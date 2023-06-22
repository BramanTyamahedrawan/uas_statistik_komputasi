import pandas as pd

df = pd.read_csv("E:\\Program\\Python\\uas-statistik\\Walmart.csv")

correlation = df.corr(numeric_only=True)["Weekly_Sales"]
threshold = 0.1
independent_vars = correlation[abs(correlation) >= threshold].index.tolist()
dependent_var = "Weekly_Sales"

print("Variabel Independen:")
print(independent_vars)
print("Variabel Dependen:")
print(dependent_var)
