import pandas as pd

df = pd.read_csv("data/frutas.csv", encoding="utf-8")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df.describe())
print(df.duplicated().sum())
print(df.drop_duplicates())
df["total"] = df["cantidad"] * df["precio"]
print(df[["fruta", "cantidad", "precio", "total"]])