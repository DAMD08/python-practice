numeros = [3, 1, 3, 4, 1, 5, 7, 8, 5, 2, 8, 9, 7, 6]

#Como en C++
maximo = numeros[0]
minimo = numeros[0]
for x in numeros:
	if x > maximo:
		maximo = x
	if x < maximo:
		minimo = x 
print(maximo, minimo)
#Con funciones integradas
print(max(numeros), min(numeros))

#Vocales de una frase
frase = "Aprendiendo Python con C++, mientras utilizo Claude como mi ayudante para ir entendiendo los temas que se van evaluando"
vocales = 0
for letra in frase.lower():
	if letra in "aeiou":
		vocales += 1
print(f"Vocales: {vocales}")
