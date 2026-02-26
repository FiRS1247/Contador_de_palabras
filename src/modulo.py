# Importaciones
import re
import tkinter as tk
from collections import Counter
from pathlib import Path
from tkinter import filedialog


# Infraestructura
def seleccionar_archivo() -> Path | None:
    # Crea ventana invisible solo para el diálogo
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal, solo muestra el diálogo

    ruta_str = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
    )

    root.destroy()

    if not ruta_str:  # El usuario cerró el diálogo sin seleccionar
        return None

    return Path(ruta_str)


def obtener_ruta():
    ruta = seleccionar_archivo()
    if not ruta:
        print("No seleccionaste ningún archivo")
        exit()
    print(f"Seleccionaste: {ruta.name}")

    return ruta


def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except UnicodeDecodeError:
        print(f"Error: '{ruta.name}' no es un archivo de texto legible.")
        exit()
    except PermissionError:
        print(f"Error: sin permiso para leer '{ruta.name}'.")
        exit()


# Dominio
def generar_lista_palabras(contenido):
    lista_palabras = re.sub(r"[^\w\s]", " ", contenido)
    return lista_palabras.lower().split()


def generar_diccionario_palabras(lista_palabras):
    diccionario_palabras = Counter(lista_palabras)
    return diccionario_palabras


def palabras_mas_comunes(diccionario_palabras, numero):
    palabras_comunes = diccionario_palabras.most_common(numero)
    return palabras_comunes


def repeticion_de_palabra(diccionario_palabras, palabra):
    repeticion_palabra = diccionario_palabras[palabra]
    return repeticion_palabra


# Servicios
def obtener_listado_palabras(lista_palabras):
    print(lista_palabras)


def palabras_comunes(diccionario_palabras):
    print("Cuantas son las palabras comunes que quieres conocer?")
    numero = input()
    num = int(numero)
    palabras_comunes = palabras_mas_comunes(diccionario_palabras, num)
    print(f"Estas son las {numero} palabras mas comunes: {palabras_comunes}")


def repetida_palabra(diccionario_palabras):
    print("Cual es la palabra repetida que quieres conocer?")
    palabra: str = input()
    repeticion_palabra = repeticion_de_palabra(diccionario_palabras, palabra)
    print(repeticion_palabra)


def main():
    # 1. Infraestructura obtiene los datos UNA vez
    ruta = obtener_ruta()
    contenido = leer_archivo(ruta)  # ← solo lee, no limpia

    # 2. Dominio los transforma
    lista_palabras = generar_lista_palabras(contenido)  # ← solo limpia, no lee
    diccionario_palabras = generar_diccionario_palabras(lista_palabras)

    # 3. Servicios muestran resultados
    obtener_listado_palabras(lista_palabras)
    palabras_comunes(diccionario_palabras)
    repetida_palabra(diccionario_palabras)


if __name__ == "__main__":
    main()
