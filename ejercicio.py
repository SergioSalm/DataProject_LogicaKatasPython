from src import UsuarioBanco
from src import Excepciones
from functools import reduce
import math
from datetime import datetime

# Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. 
# Tiene que devolver un diccionario.
def contar_palabras(texto):
    """
    Función que a partir de un texto pasado por parámentro, cuenta cuantas veces se repiten las mismas palabras dentro del texto

    Args:
        texto (str): texto al que contar las palabras repetidas

    Returns:
        dict: Devolvemos un diccionario con las palabras y el número de veces que sale en el texto
    """
    dict_palabras = {}
    lista_palabras = "".join(texto).split(" ")

    #eliminamos duplicados
    set_palabras = set(lista_palabras)

    for palabra in set_palabras:
        dict_palabras[palabra] = lista_palabras.count(palabra)

    return dict_palabras

# Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva.
# Tiene que devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto, palabra_original, palabra_reemplazo):
    """
    Función que a partir de un texto pasado por parámetro, reemplaza la palabra (si existe en el texto) pasada por parámentro, por otra palabra también pasada por parámetros

    Args:
        texto (str): texto original
        palabra_original (str): palabra que queremos cambiar
        palabra_reemplazo (str): palabra nueva que queremos en el texto

    Returns:
        str: texto con las palabras cambiadas
    """
    texto_reemplazado = texto.replace(palabra_original, palabra_reemplazo)
    return texto_reemplazado

# Crear una función eliminar_palabra para eliminar una palabra del texto.
# Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Función que a partir de un texto pasado por parámetro, elimina la palabra (si existe en el texto) pasada por parámentro

    Args:
        texto (str): texto original
        palabra_a_eliminar (str): palabra que queremos eliminar

    Returns:
        str: texto con las palabras eliminada
    """

    lista_palabras = "".join(texto).split(" ")
    lista_palabra_eliminada = list(filter(lambda palabra: palabra != palabra_a_eliminar, lista_palabras))
    #texto_palabra_eliminada = texto.replace(palabra_a_eliminar, "") Opción descartada porque deja un espacio en la palabra eliminada

    texto_palabra_eliminada = " ".join(lista_palabra_eliminada)
    return texto_palabra_eliminada

# Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") 
# y un número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
def procesar_texto(texto, opcion, *kargs):
    """
    Función que procesa un texto según la opción que se le pasa por parámetro

    Args:
        texto (str): texto original a procesar
        opcion (str): opción a realizar ("contar", "reemplazar", "eliminar")
        *kargs: argumentos opcionales necesarios o no en función de la opción elegida
    Raises:
        ValueError: Error por no pasar dos argumentos en la opción reemplazar
        ValueError: Error por pasar un argumento en la opción eliminar
        ValueError: Error por pasar una opción no contemplada

    Returns:
        dict, str: resultado de la operación indicada. Contar -> Diccionario; reemplazar y eliminar -> str
    """

    try:
        if opcion.lower() == "contar":
            return contar_palabras(texto)
        elif opcion.lower() == "reemplazar":
            if len(kargs) != 2:
                raise ValueError(f"La opción {opcion} necesita 2 paramétros y solamente se han pasado {len(kargs)}")
            return reemplazar_palabras(texto, kargs[0], kargs[1])
        elif opcion.lower() == "eliminar":
            if len(kargs) != 1:
                raise ValueError(f"La opción {opcion} necesita 1 paramétros y solamente se han pasado {len(kargs)}")
            return eliminar_palabra(texto, kargs[0])
        else:
            raise ValueError(f"Opción {opcion} no contemplada. Las opciones son 'contar', 'reemplazar' o 'eliminar'")
    except ValueError as e:
        print(e)



texto = "Frisaba la edad de nuestro hidalgo con los cincuenta años: era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "cincuenta"))
print(procesar_texto(texto, "reemplazar", "cincuenta", "cuarenta"))
print(procesar_texto(texto, "eliminar"))
print(procesar_texto(texto, "eliminar", "de"))
print(procesar_texto(texto, "otro", "de"))

