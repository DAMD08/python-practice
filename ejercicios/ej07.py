def leer_texto(ruta):
	try:
		with open(ruta, "r", encoding="utf-8") as archivo:
			contenido = archivo.read()
		contenido_minusculas = contenido.lower()
		for signo in [".", ",", ";", ":"]:
			contenido_minusculas = contenido_minusculas.replace(signo, "")
		palabras = contenido_minusculas.split()
		return palabras
	except FileNotFoundError:
		print(f"Error: No se encontro el archivo '{ruta}'. Asegurate que este en la misma carpeta")
		return[]

def contar(palabras):
	ignorar = ["las", "los", "como", "del", "que", "sus", "una"]
	conteo = {}
	for palabra in palabras:
		if palabra in ignorar: continue
		if len(palabra) >= 4:
			if palabra in conteo:
				conteo[palabra] += 1
			else:
				conteo[palabra] = 1
	return conteo

def top(conteo, n):
	# .items() convierte el diccionario en tuplas (palabras, frecuencia)
	# lambda toma cada "par" y selecciona el elemento para ordenar 
	palabras_ordenadas = sorted(conteo.items(), key=lambda par: par[1], reverse=True)
	print(f"\n --- Las {n} palabras mas frecuentes ---")
	for palabra, frecuencia in palabras_ordenadas[:n]:
			print(f"- {palabra}: {frecuencia} veces")

if __name__ == "__main__":
	ruta_archivo = "ejercicios/texto.txt"
	lista_palabras = leer_texto(ruta_archivo)
	if lista_palabras:
		diccionario_conteo = contar(lista_palabras)
		top(diccionario_conteo, 10)
