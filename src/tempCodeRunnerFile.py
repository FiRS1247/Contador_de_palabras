print(f"Seleccionaste: {ruta.name}")
with open(ruta, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

filtrado = re.sub(r"[^\w\s]", " ", contenido)
palabras = filtrado.lower().split()

print(palabras)
print(len(palabras))