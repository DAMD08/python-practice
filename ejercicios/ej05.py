def es_primo(n):
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

def primos_hasta(n):
	resultado = []
	for i in range(2, n + 1):
		if es_primo(i):
			resultado.append(i)
	return resultado

if __name__ == "__main__":
	n = int(input("Hasta: "))
	print(primos_hasta(n))
