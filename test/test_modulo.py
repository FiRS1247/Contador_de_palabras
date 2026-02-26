import sys
from collections import Counter
from pathlib import Path

# Le dice a Python dónde buscar módulos — la carpeta raíz del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.modulo import (
    generar_diccionario_palabras,
    generar_lista_palabras,
    palabras_mas_comunes,
    repeticion_de_palabra,
)


def test_generar_lista_palabras():

    contenido = "Hola, Python, Hola Mundo"
    resultado = generar_lista_palabras(contenido)

    assert resultado == ["hola", "python", "hola", "mundo"]


def test_generar_diccionario_palabras():

    contenido: list[str] = ["hola", "python", "hola", "mundo"]

    resultado = generar_diccionario_palabras(contenido)

    assert resultado == {"hola": 2, "python": 1, "mundo": 1}


def test_palabras_mas_comunes():
    contenido = Counter({"hola": 2, "python": 1, "mundo": 1})
    resultado = palabras_mas_comunes(contenido, 2)
    assert resultado == [("hola", 2), ("python", 1)]


def test_repeticion_de_palabra():

    contenido = Counter({"hola": 2, "python": 1, "mundo": 1})

    resultado = repeticion_de_palabra(contenido, "hola")

    assert resultado == 2
