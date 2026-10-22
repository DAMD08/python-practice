import pandas as pd

ventas = pd.DataFrame({
    "fruta": ["fresa", "mora", "fresa", "sandia", "kiwi"],
    "cantidad": [4, 5, 6, 2, 4]
})

precios = pd.DataFrame({
    "fruta": ["fresa", "mora", "naranja", "sandia"],
    "precio": [0.5, 0.75, 0.6, 0.4]
})

print(pd.merge(ventas, precios, on="fruta", how="inner"))
print(pd.merge(ventas, precios, on="fruta", how="left"))
print(pd.merge(ventas, precios, on="fruta", how="right"))
print(pd.merge(ventas, precios, on="fruta", how="outer"))