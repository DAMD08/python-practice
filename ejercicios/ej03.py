x = int(input("Numero: "))

#parte 1
for i in range(1, 11):
	rs = x * i 
	print(f"{x} * {i} = {x * i}")
#parte 2
n = int(input("Suma hasta: "))
suma = 0
for i in range(1, n + 1):
	suma += i
	print(f"{n} + {i} = {suma}")

print(f"Suma con bucle: {suma}")
print(f"Suma con sum(): {sum(range(1, n + 1))}")
