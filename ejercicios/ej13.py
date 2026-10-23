import pandas as pd

RUTA = "data/raw/소상공인시장진흥공단_상가(상권)정보_경기_202606.csv"
df = pd.read_csv(RUTA, encoding="utf-8", nrows=50000, low_memory=False)

df = df.sample(50000, random_state=42)
top = (
    df.groupby('상권업종대분류명')
    .size()
    .sort_values(ascending=False, kind="stable")
    .head(10)
)
print("Top 10 categorías de '상권업종대분류명' con más registros:")
print(top)
print("-" * 40)

print("Lista de columnas disponibles en el DataFrame:")
print(df.columns.tolist())
print("-" * 40)

columna_ciudad = "시군구명"
if columna_ciudad in df.columns:
    top_ciudades = (
        df.groupby(columna_ciudad)
        .size()
        .sort_values(ascending=False, kind="stable")
        .head(10)

    )
    print(f"Top 10 ciudades con más registros en la columna '{columna_ciudad}':")
    print(top_ciudades)
print("-" * 40)

print(df.dtypes[["상권업종대분류명", "경도", "위도"]])

df["상권업종대분류명"] = df["상권업종대분류명"].astype("string")
df["경도"] = pd.to_numeric(df["경도"], errors="coerce")
df["위도"] = pd.to_numeric(df["위도"], errors="coerce")

print("Tipos de datos después de la conversión:")
print(df.dtypes[["상권업종대분류명", "경도", "위도"]])