import sqlite3

con = sqlite3.connect("data/tiendas.db")
cur = con.cursor()

for fila in cur.execute("PRAGMA table_info(tiendas)"):
    print(fila[1]) # Imprime el nombre de cada columna

consulta = """
With por_ciudad AS (
    SELECT "시군구코드" AS ciudad, COUNT(*) AS total_tiendas
    FROM tiendas
    GROUP BY "시군구코드"
)
SELECT ciudad, total_tiendas
FROM por_ciudad
WHERE total_tiendas > 500
ORDER BY total_tiendas DESC
"""

for fila in cur.execute(consulta):
    print(fila[0], fila[1]) # Imprime el nombre de la ciudad y el total de tiendas

consulta2 = """
With por_ciudad AS (
    SELECT "시군구코드" AS ciudad, COUNT(*) AS total_tiendas
    FROM tiendas
    GROUP BY "시군구코드"
)
SELECT AVG(total_tiendas) AS promedio_tiendas, MIN(total_tiendas) AS min_tiendas, MAX(total_tiendas) AS max_tiendas
FROM por_ciudad
WHERE total_tiendas > 500
ORDER BY total_tiendas DESC
LIMIT 5
"""

for fila in cur.execute(consulta2):
    print(f"Promedio de tiendas: {fila[0]}, Mínimo de tiendas: {fila[1]}, Máximo de tiendas: {fila[2]}")

consulta3 = """
With por_ciudad AS (
    SELECT "시군구코드" AS ciudad, COUNT(*) AS total_tiendas
    FROM tiendas
    GROUP BY "시군구코드"
)
SELECT ciudad, total_tiendas
FROM por_ciudad
WHERE total_tiendas < 500 AND total_tiendas != 0
ORDER BY total_tiendas DESC
LIMIT 5
"""

for fila in cur.execute(consulta3):
    print(fila[0], fila[1]) # Imprime el nombre de la ciudad y el total de tiendas

cols = [fila[1] for fila in cur.execute("PRAGMA table_info(tiendas)")]
print("Columnas de la tabla 'tiendas':", len(cols))
print([(c, repr(c)) for c in cols if "시군구" in c]) # Imprime el nombre de cada columna y su representación

consulta4 = """
With por_ciudad AS (
    SELECT "시군구명" AS ciudad, COUNT(*) AS total_tiendas
    FROM tiendas
    GROUP BY "시군구명"
),
promedios AS (
    SELECT AVG(total_tiendas) AS promedio_tiendas, MIN(total_tiendas) AS min_tiendas, MAX(total_tiendas) AS max_tiendas
    FROM por_ciudad
)
SELECT ciudad, total_tiendas
FROM por_ciudad, promedios
WHERE total_tiendas > promedio_tiendas
ORDER BY total_tiendas DESC
"""
for fila in cur.execute(consulta4):
    print(fila[0], fila[1]) # Imprime el nombre de la ciudad y el total de tiendas