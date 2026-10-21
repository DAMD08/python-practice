while True:
	try:
		n = int(input("Numero: "))
		break
	except ValueError:
		print("No es un numero entero, intenta de nuevo.")
print(f"Escribiste: {n}")
