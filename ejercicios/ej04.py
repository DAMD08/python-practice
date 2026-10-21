n = int(input("Numero: "))
pasos = 0 

while n != 1:
	if n % 2 == 0:
		n = n // 2
	else:
		n = 3 * n + 1
	print(n)
	pasos += 1

print(f"Pasos: {pasos}")
