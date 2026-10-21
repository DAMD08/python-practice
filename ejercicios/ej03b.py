x = int(input("Numero: "))

#imprimir solo los impares
par = 0
for i in range(1, x + 1):
	par = i	
	if(par % 2 == 0):
		print(f"{par} es par")
#factorial
n = int(input("Numero!: "))
factorial = 1
for i in range(1, n + 1):
	factorial *= i

print(f"{n}! = {factorial}")
