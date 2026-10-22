import pandas as pd

df = pd.DataFrame({
	"fruta": ["fresa", "mora", "fresa", "naranja", "sandia", "sandia"],
	"cantidad": [4, 5, 6, 1, 2, 4],
})

print(df)
print(df[df["cantidad"] > 3])
print(df.dtypes)
print(df["cantidad"].sum())
print(df.groupby("fruta")["cantidad"].sum())
print(df.groupby("fruta")["cantidad"].mean())
print(df.groupby("fruta")["cantidad"].max())
print(df.groupby("fruta")["cantidad"].min())
print(df.groupby("fruta")["cantidad"].count())

