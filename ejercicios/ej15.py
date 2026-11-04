import sqlite3
import pandas as pd

RUTA = "data/raw/소상공인시장진흥공단_상가(상권)정보_경기_202606.csv"

df = pd.read_csv(RUTA, encoding="utf-8", low_memory=False, dtype=str)
print(df.shape) # Imprime la cantidad de filas y columnas del DataFrame

df["경도"] = pd.to_numeric(df["경도"], errors="coerce") # Convierte la columna "경도" a tipo numérico, reemplazando errores con NaN
df["위도"] = pd.to_numeric(df["위도"], errors="coerce")

con = sqlite3.connect("data/tiendas.db")
df.to_sql("tiendas", con, if_exists="replace", index=False) # Guarda el DataFrame en la base de datos SQLite, reemplazando la tabla si ya existe

print("Datos guardados en la base de datos SQLite 'tiendas.db' en la tabla 'tiendas'.")
print(len(list(con.execute("PRAGMA table_info(tiendas)")))) # Imprime la cantidad de columnas de la tabla "tiendas"
print(con.execute('SELECT typeof("경도") AS tipo, COUNT(*) AS conteo FROM tiendas GROUP BY tipo').fetchall()) # Imprime la cantidad de filas de la tabla "tiendas"

consulta_ciudades = """
WITH por_ciudad AS (
    SELECT 시도코드, COUNT(*) AS total_tiendas
    FROM tiendas
    GROUP BY 시도코드
)
SELECT 시도코드, total_tiendas
FROM por_ciudad
ORDER BY total_tiendas DESC

"""
resultado_ciudades = con.execute(consulta_ciudades).fetchall()
print("Número de tiendas por ciudad (ordenadas de mayor a menor):")
for ciudad, total in resultado_ciudades:
    print(f"{ciudad}: {total}")