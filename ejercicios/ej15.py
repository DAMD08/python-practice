import sqlite3
import pandas as pd

RUTA = "data/raw/소상공인시장진흥공단_상가(상권)정보_경기_202606.csv"
cols = ["건물관리번호", "지번코드", "도로명코드", "행정동코드", "법정동코드", "시군구코드", "시도코드", "신우편번호", "구우편번호"]


df = pd.read_csv(RUTA, encoding="utf-8", low_memory=False, dtype={col: "string" for col in cols}, usecols=cols)
muestra = df.sample(50000, random_state=42)

con = sqlite3.connect("data/tiendas.db")
muestra.to_sql("tiendas", con, if_exists="replace", index=False)

consulta = "SELECT typeof(건물관리번호) AS tipo, COUNT(*) AS conteo FROM tiendas GROUP BY tipo"
resultado = con.execute(consulta).fetchall()

print("Tipos de datos y conteo de registros en la base de datos:")
for tipo, count in resultado:
    print(f"{tipo}: {count}")