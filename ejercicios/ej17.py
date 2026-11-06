import sqlite3

con = sqlite3.connect("data/tiendas.db")
cur = con.cursor()

consulta = """
    WITH c AS (
        SELECT "시군구명" AS ciudad, 상가업소번호 AS tienda, ROW_NUMBER() OVER (PARTITION BY "시군구명" ORDER BY 상가업소번호 DESC) AS ranking
        FROM tiendas
        GROUP BY "시군구명"
    )
    SELECT ciudad, tienda, ranking
    FROM c
    LIMIT 5;
"""
print("Ciudades con más tiendas con ROW_NUMBER():")
cur.execute(consulta)
for fila in cur.fetchall():
    print(fila[0], fila[1], fila[2]) # Imprime el nombre de la ciudad, el total de tiendas y su ranking


consulta2 = """
    WITH c AS (
        SELECT "시군구명" AS ciudad, COUNT(*) AS total_tiendas
        FROM tiendas
        GROUP BY "시군구명"
    )
    SELECT ciudad, total_tiendas, RANK() OVER (ORDER BY total_tiendas DESC) AS ranking
    FROM c
    LIMIT 5;
"""

print("\nCiudades con más tiendas (con ranking):")
cur.execute(consulta2)

for fila in cur.fetchall():
    print(fila[0], fila[1], fila[2]) # Imprime el nombre de la ciudad, el total de tiendas y su ranking

consulta3 = """
    WITH c AS (
        SELECT "시군구명" AS ciudad, COUNT(*) AS total
        FROM tiendas
        GROUP BY "시군구명"
    )
    SELECT ciudad, total, 
        LAG(total) OVER (ORDER BY total DESC) AS tiendas_anterior,
        LAG(total) OVER (ORDER BY total DESC) - total AS diferencia_anterior,
        total * 100.0 / LAG(total) OVER (ORDER BY total DESC) AS porcentaje_anterior,
        LEAD(total) OVER (ORDER BY total DESC) AS tiendas_siguiente
    FROM c
    LIMIT 5;
"""

print("\nCiudades con más tiendas (con LAG y LEAD):")
cur.execute(consulta3)
for fila in cur.fetchall():
    print(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]) # Imprime el nombre de la ciudad, el total de tiendas, el total de tiendas de la ciudad anterior, la diferencia con la ciudad anterior y el total de tiendas de la ciudad siguiente

consulta4 = """
    WITH c AS (
        SELECT "시군구명" AS ciudad, COUNT(*) AS total
        FROM tiendas
        GROUP BY "시군구명"
        
    ),
    a AS (
        SELECT ciudad, total,
            SUM(total) OVER (ORDER BY total DESC) AS acum,
            SUM(total) OVER () AS total_general,
            SUM(total) OVER (ORDER BY total DESC) * 100.0 / SUM(total) OVER () AS pct_acum
        FROM c
    )
    SELECT ciudad, total, acum, total_general, pct_acum, count(*) OVER () AS total_ciudades
    FROM a
    WHERE pct_acum >= 50
    LIMIT 10;
"""

print("\nCiudades con más tiendas (con SUM y porcentaje acumulado):")
cur.execute(consulta4)
for fila in cur.fetchall():
    print(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]) # Imprime el nombre de la ciudad, el total de tiendas, el acumulado, el total general y el porcentaje acumulado