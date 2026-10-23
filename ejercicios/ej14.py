import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    salario REAL NOT NULL
)''')
cur.execute('''
CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
)''')

cur.executemany('INSERT INTO empleados (nombre, salario) VALUES (?, ?)', [
    ('Alice', 70000),
    ('Bob', 80000),
    ('Charlie', 90000),
    ('Diana', 60000),
    ('Eve', 75000),
    ('Frank', 85000),
    ('Grace', 95000),
    ('Heidi', 72000),
    ('Ivan', 88000),
    ('Judy', 77000),
    ('Kevin', 81000),
])
cur.executemany('INSERT INTO departamentos (nombre) VALUES (?)', [
    ('Recursos Humanos',),
    ('Desarrollo',),
    ('Ventas',),
    ('Marketing',),
    ('Finanzas',),
    ('Atención al Cliente',),
    ('Logística',),
]) 

#
print("Empleados:")
cur.execute('SELECT * FROM empleados')
for row in cur.fetchall():
    print(row)

print("\nDepartamentos:")
cur.execute('SELECT * FROM departamentos')
for row in cur.fetchall():
    print(row)

print("\nEmpleados con salario mayor a 75000:")
cur.execute('SELECT * FROM empleados WHERE salario > 75000')
for row in cur.fetchall():
    print(row)

print("\nEmpleados ordenados por salario descendente:")
cur.execute('SELECT * FROM empleados ORDER BY salario DESC')
for row in cur.fetchall():
    print(row)
print("\nEmpleados con salario mayor a 75000 y ordenados por salario descendente:")
cur.execute('SELECT * FROM empleados WHERE salario > 75000 ORDER BY salario DESC')
for row in cur.fetchall():
    print(row)

print("\nEmpleados con salario mayor a 75000 y GROUP BY departamento:")
cur.execute('''
SELECT d.nombre AS departamento, COUNT(e.id) AS num_empleados, AVG(e.salario) AS salario_promedio
FROM empleados e
LEFT JOIN departamentos d ON e.id = d.id
WHERE e.salario > 75000
GROUP BY d.nombre
''')
for row in cur.fetchall():
    print(row)

print("\nEmpleados con salario mayor a 75000 y ordenados por salario descendente (usando JOIN):")
cur.execute('''
SELECT e.id, e.nombre, e.salario, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.id = d.id
WHERE e.salario > 75000
ORDER BY e.salario DESC
''')
for row in cur.fetchall():
    print(row)

print("\nEmpleados con salario mayor a 75000 y ordenados por salario descendente (usando JOIN y subconsulta):")
cur.execute('''
SELECT e.id, e.nombre, e.salario, d.nombre AS departamento
FROM empleados e
LEFT JOIN (SELECT id, nombre FROM departamentos
) d ON e.id = d.id
WHERE e.salario > 75000
ORDER BY e.salario DESC
''')
for row in cur.fetchall():
    print(row)

print("\nEmpleados con salario mayor a 75000 y ordenados por salario descendente (usando JOIN y subconsulta con alias):")
cur.execute('''
SELECT e.id, e.nombre, e.salario, d.nombre AS departamento
FROM empleados e
LEFT JOIN (SELECT id, nombre FROM departamentos) AS d ON e.id = d.id
WHERE e.salario > 75000
ORDER BY e.salario DESC
''')
for row in cur.fetchall():
    print(row)
