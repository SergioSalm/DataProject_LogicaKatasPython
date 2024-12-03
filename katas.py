#Importación cálculos matemáticos
import math
#Importación fecha hora
from datetime import datetime
#importación función reduce
from functools import reduce

#importación de las clases 
from src import Arbol
from src import UsuarioBanco
from src import Excepciones


# 1- Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
#    Los espacios no deben ser considerados.
def frecuencia_letras(cadena):
    """
    Esta función recibe una cadena de texto como parámetro y devuelve un diccionario con las frecuencias de cada letra en la cadena. 

    Args:
        cadena (str): cadena de texto a analizar

    Returns:
        dict: devuelve un diccionario con la frecuencia de cada letra en la cadena.
    """
    diccionario_frecuencia_letras = dict()

    for letra in cadena:
        #Si es un espacio, no lo tenemos en cuenta
        if (letra == ' '):
            continue

        if letra in diccionario_frecuencia_letras:
            diccionario_frecuencia_letras[letra] += 1
        else:
            diccionario_frecuencia_letras[letra] = 1

    return diccionario_frecuencia_letras

cadena_texto = "El ingenioso hidalgo don Quijote de la Mancha"

print(f"La cadena de texto es {cadena_texto}")
print(f"Frecuencua de la cadena: {frecuencia_letras(cadena_texto)}")


# 2- Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
lista_numero =[1,2,3,4,5,6,7,8,9,10]

def dobla_valor(numero):
    """
    Función que devuelve el doble del número que viene por parámentro
    
    Args:
        numero (int o float): número que vamos a doblar

    Returns:
        int o float: valor doble del número que recibimos por parámetro
    """
    return numero * 2

print(f"Lista original: {lista_numero}")
print(f"Lista doblada:  {list(map(dobla_valor, lista_numero))}")


# 3- Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
#    La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def encuentra_palabra_objetivo(lista_palabras, palabra_objetivo):
    """
    Esta función recibe una lista de palabras y un texto a buscar dentro de las palabras de la lista. 
    Devuelve una lista con todas las palabras que tienen la palabra objetivo.
    Args:
        lista_palabras (list): lista de palabras
        palabra_objetivo (string): palabra a buscar

    Returns:
        list: lista con las palabras que contienen la palabra objetivo
    """
    lista_palabras_objetivo = list()

    for palabra in lista_palabras:
        #Si no encuentra el valor, el find devuelve -1
        if palabra.find(palabra_objetivo) > 0:
            lista_palabras_objetivo.append(palabra)

    return lista_palabras_objetivo

palabras = ['caminando', 'ordenador', 'flipado', 'tornado', 'volando']
objetivo = 'ando'

print(f"Palabras de la lista: {palabras}")
print(f"Texto a encontrar: {objetivo}")
print(f"Palabras que contienen el texto: {encuentra_palabra_objetivo(palabras, objetivo)}")


# 4- Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_valores_listas(valor_lista1, valor_lista2):
    """Función que devuelve la diferencia entre los valores de dos listas. 

    Args:
        valor_lista1 (list): lista de números
        valor_lista2 (list): lista de números

    Returns:
        list: nueva lista con la diferencia entre las dos lista
    """
    return valor_lista1 - valor_lista2

lista_1 = [10,9]
lista_2 = [1,2]
print(f"Valores lista 1: {lista_1}")
print(f"Valores lista 2: {lista_2}")
print(f"Lista con la diferencia: {list(map(diferencia_valores_listas, lista_1, lista_2))}")

lista_3 = [10,9,8]
lista_4 = [2,3]
print(f"Valores lista 3: {lista_3}")
print(f"Valores lista 4: {lista_4}")
print(f"Lista con la diferencia: {list(map(diferencia_valores_listas, lista_3, lista_4))}")

lista_5 = [10,9]
lista_6 = [4, 5, 6]
print(f"Valores lista 5: {lista_5}")
print(f"Valores lista 6: {lista_6}")
print(f"Lista con la diferencia: {list(map(diferencia_valores_listas, lista_5, lista_6))}")


# 5- Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
#    La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
#    Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
#    La función debe devolver una tupla que contenga la media y el estado.
def calcula_aprobado_suspenso(lista_numeros, nota_aprobado = 5):
    """
    Función que calcula la media de los valores de la lista lista_numeros y valida si está por encima o por debajo de la nota_nota_aprobado
    Si la media está por encima de la nota_aprobado, el estado será "aprobado", de lo contrario, será "suspenso".

    Args:
        lista_numeros (list): lista de números para calcular la media.
        nota_aprobado (int, optional): nota a partir de la cual se aprueba. Defaults to 5.

    Returns:
        tupla: Devolvemos la media de las notas de la lista con el estado(aprobado o suspenso).
    """
    media = sum(lista_numeros) / len(lista_numeros)
    
    #Vamos a ser positivos, e inicializamos la variable con aprobado.
    estado = 'aprobado'
    
    if (media < nota_aprobado):
        estado = 'suspenso'      

    return (media, estado)
    
lista_notas = [1,2,3,4,5,6]

resultado = calcula_aprobado_suspenso(lista_notas)
print(f"Las notas son {lista_notas}")
print(f"El estado es {resultado[1]}, con una media de {resultado[0]}")

resultado = calcula_aprobado_suspenso(lista_notas, 3)
print(f"Las notas son {lista_notas}")
print(f"El estado es {resultado[1]}, con una media de {resultado[0]}")


# 6- Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero):
    """
    Función que calcula el factorial de un número de forma recursiva

    Args:
        numero (int): número a calcular

    Returns:
        int: factorial del número pasado como parámentro
    """
    if numero == 1:
        return 1 
    else:
        return numero * factorial(numero - 1)

    
numero = 10
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

# 7- Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_lista(tupla_a_convertir):
    """
    Función que convierte una lista de tuplas a una lista de strings

    Args:
        tupla_a_convertir (tuple): tupla a convertir

    Returns:
        list: lista convertida a string
    """
    lista_convertida = map(str, tupla_a_convertir)
    lista_convertida = " ".join(lista_convertida)
    return lista_convertida

tupla = [(1,3),("Manzana", "Roma"), (1,"Madrid"), (2,"Barcelona")]
lista = list(map(tuplas_a_lista, tupla))
print(lista)

 
# 8- Escribe un programa que pida al usuario dos números e intente dividirlos. 
#    Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. 
#    Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
try:
    dividendo = float(input("Introduce el dividendo: "))
    divisor = float(input("Introduce el divisor: "))

    resultado = dividendo / divisor
    print(f"El resultado de dividir {dividendo} entre {divisor} es {resultado}")

except ZeroDivisionError:
   print("No se puede dividir por cero")
except ValueError:
    print("Solamente se pueden introducir números")


# 9- Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def excluir_animales_prohibidos_ESP(mascota):
    """
    Función que excluye los animales considerados prohibidos de una lista

    Args:
        mascota (string): mascota para revisar si está prohibida

    Returns:
        bool: Devuelve True si la mascota no está prohibida. False si la mascota está prohibida
    """
    lista_mascotas_excluir = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    if mascota in lista_mascotas_excluir:
        return False
    return True

lista_mascotas = ["Perro", "Pájaro", "León", "Oso", "Jabalí", "Tigre", "Oso panda"]
lista_mascotas_permitidas = list(filter(excluir_animales_prohibidos_ESP, lista_mascotas))
print(f"Lista de mascotas: {lista_mascotas}")
print("Mascotas de la lista permitidas en España: ", lista_mascotas_permitidas)


# 10- Escribe una función que reciba una lista de números y calcule su promedio. 
#     Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente
def calcula_promedio(lista_numeros):
    """
    Función que reciba una lista de números y calcula el promedio de los valores

    Args:
        lista_numeros (list): lista con los valores a calcular

    Raises:
        Excepciones.ListaVacia: Excepción personalizada para controlar las listas vacías

    Returns:
        int: devuelve el promedio de los valores de la lista
    """
    if len(lista_numeros) == 0:
        raise Excepciones.ListaVacia("La lista está vacía.")
    
    return sum(lista_numeros) / len(lista_numeros)

try:
    lista_a_calcular = []
    print(f"El promedio de los valores de la lísta es de: {calcula_promedio(lista_a_calcular)}")

    lista_a_calcular = [5,10,15]
    print(f"El promedio de los valores de la lísta es de: {calcula_promedio(lista_a_calcular)}")
except Excepciones.ListaVacia as e:
    print(f"Se ha producido un error. {e}")

# 11- Escribe un programa que pida al usuario que introduzca su edad. 
#     Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.
try:
    edad = int(input("Introduce tu edad: "))

    if 0 <= edad <= 120:
        print(f"Tu edad es de {edad} años")
    else:
        raise Excepciones.EdadFueraRango("La edad debe de estar comprendida entre 0 y 120 años")
    
except Excepciones.EdadFueraRango as e:
    print(f"Error. {e}")
except ValueError:
    print(f"El valor introducido no es numérico")


# 12- Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabra(frase):
    """
    Función que recibe una frase y devuelve una lista con la longitud de cada palabra

    Args:
        frase (str): frase

    Returns:
        lista: lista con la palabra y su longitud.
    """
    palabras = frase.split()
    
    #lista_longitud = list(map(str, palabras), map(len, palabras))
    lista_longitud = list(map(lambda palabra: (palabra, len(palabra)), palabras))
        
    return lista_longitud

frase = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."

lista_longitud_palabras = longitud_palabra(frase)
print(lista_longitud_palabras)


# 13- Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
#     Las letras no pueden estar repetidas .Usa la función map()
def letras_mayusculas_minusculas(caracteres):
    """Función que devuelve una lista de tuplas con las letras en mayúscula y minúscula a partir de un conjunto de carácteres, sin repetir letras

    Args:
        caracteres (str): conjunto de caracteres

    Returns:
        lista_: lista de tuplas con cada letra en mayúsculas y minúsculas. 
    """
    set_letras_unicas = set()
    exclusion = " ,.¡!¿?"

    #Quitamos espacios y símbolos
    for letra in caracteres:
        if letra.isalpha and letra not in exclusion:
            set_letras_unicas.add(letra)

    lista_caracteres = list(map(lambda letra: (letra.upper(), letra.lower()), set_letras_unicas))
    
    return lista_caracteres

frase = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."

print(letras_mayusculas_minusculas(frase))


# 14- Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def filtrar_palabras(lista_palabras, letra_filtro):
    """
    Función que devuelve las palabras de una lista de palabras que comiencen con una letra en especifico

    Args:
        lista_palabras (list): lista de palabras
        letra_filtro (str): letra a filtrar

    Returns:
        list: devuelve una lista con las palabras de la lista_palabras que empiezan con la letra_filtro
    """
    lista_filtrada = list(filter(lambda palabra: palabra[0] == letra_filtro , lista_palabras))

    return lista_filtrada


lista_palabras = ["uno", "dos", "torpedo", "guante", "firulais"]
letra_filtro = "f"
print (f"Lista de palabras: {lista_palabras}")
print (f"Palabaras que empiezan por {letra_filtro}: {filtrar_palabras(lista_palabras, letra_filtro)}")
 

# 15- Crea una función lambda que  sume 3 a cada número de una lista dada.
funcion_suma_3 = lambda lista: [numero + 3 for numero in lista]

lista_numeros = [1,3,6,9]
lista_sumada = funcion_suma_3(lista_numeros)

print(f"Lista original: {lista_numeros}")
print(f"Lista sumada: {lista_sumada}")

 
# 16- Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def filtra_palabras_longitud(cadena_texto, longitud):
    """
    Función que devuelve una lista a partir de las palabras de la cadena de texto que pasamos por parámetro, y tienen una longitud superior a la indicada por parámetro

    Args:
        cadena_texto (str): cadena de texto
        longitud (int): longitud a tener en cuenta

    Returns:
        list: lista con las palabras que tienen una longitud superior a 'longitud'
    """
    palabras_cadena = cadena_texto.split()
    
    lista_palabras_longitud = list(filter(lambda palabra: len(palabra) > longitud, palabras_cadena))
    
    return lista_palabras_longitud

cadena = "Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera"
longitud = 6

print(f"Frase a calcular: {cadena}")
print(f"Las palabras que tienen una longitud supuerior a {longitud} caracteres, son: {filtra_palabras_longitud(cadena, longitud)}")


# 17- Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
#     Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()
def convertir_lista_a_numero(lista_numeros):
    """
    Función que a partir de una lista que contiene números, devuelve el número correspondiente
    Args:
        lista_numeros (list): lista de números

    Returns:
        int: número correspondiente a partir de la lista
    """
    return int(reduce(lambda num1,num2: str(num1)+str(num2), lista_numeros))

lista_numeros = [2,4,56,3]
print(f"La lista de números es: {lista_numeros}")
print(f"Número correspondiente: {convertir_lista_a_numero(lista_numeros)}")


# 18- Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) 
#     y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.Usa la función filter()
estudiantes = [
    {"nombre": "Quijote", "Edad":50, "calificacion":75},
    {"nombre": "Sancho", "Edad":50, "calificacion":90},
    {"nombre": "Romeo", "Edad":16, "calificacion":92},
    {"nombre": "Julieta", "Edad":14, "calificacion":91},
    {"nombre": "Hamlet", "Edad":30, "calificacion":99},
]

print("Estudiantes a analizar: ")
for estudiante in estudiantes:
    print(estudiante)

estudiantes_de_90 = list(filter(lambda estudiante: estudiante["calificacion"] >= 90 , estudiantes))
print("Estudiantes con calificación superor a 90:")
for estudiante in estudiantes_de_90:
    print(estudiante)

# 19- Crea una función lambda que filtre los números impares de una lista dada.
funcion_calcula_numero_impar = lambda lista_numeros: [numero for numero in lista_numeros if numero % 2 != 0]

lista_numero = [1,2,3,4,5,31,32,43,45,67,88,90]
print(f"Lista de números a calcular: {lista_numero}")
print(f"Números impares de la lista: {funcion_calcula_numero_impar(lista_numero)}")


# 20- Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
funcion_filtrar_int = lambda lista: [componente for componente in lista if type(componente) == int]

lista = [1,"2",3,"casa", 5, "3434"]
print(f"Lista de valores a calcular: {lista}")
print(f"Valores de tipo int de la lista: {funcion_filtrar_int(lista)}")


# 21- Crea una función que calcule el cubo de un número dado mediante una función lambda
calcular_cubo = lambda numero: numero**3

numero = 5
cubo = calcular_cubo(5) 
print(f"El cubo de {numero} es {cubo}")


# 22- Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().
lista_numerica = [1,2,3,10]

print(f"Valores numéricos a calcular: {lista_numerica}")
resultado = reduce(lambda num1, num2: num1*num2, lista_numerica)
print(f"El producto total de los números de la lista es: {resultado}")


# 23- Concatena una lista de palabras.Usa la función reduce() .
lista_palabras = ["El", "ingenioso", "hidalgo", "don", "Quijote", "de", "la", "Mancha"]

print(f"Palabras de la lista: {lista_palabras}")
palabras_concatenadas = reduce(lambda str1, str2: str1 + " " + str2, lista_palabras)
print(f"Palabras concatenadas: {palabras_concatenadas}")


# 24- Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
lista_numerica = [50, 5, 5, 5, 10]

print(f"Lista de números a calcular: {lista_numerica}")
diferencia_total = reduce(lambda num1, num2: num1 - num2, lista_numerica)
print(f"Diferencia total de los valores de la lista: {diferencia_total}")


# 25- Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena_texto):
    """
    Función que cuenta el número de letras en una cadena de texto. No tenemos en cuenta los espacios.

    Args:
        cadena_texto (str): cadena de texto

    Returns:
        int: número de letras que contiene la cadena de texto
    """
    lista_palabras = cadena_texto.split()
    total_caracteres = 0

    for palabra in lista_palabras:
        total_caracteres += len(palabra)

    return total_caracteres


cadena_texto = "Porque ni el bien ni el mal pueden durar eternamente; y así se sigue que como el mal ha durado mucho tiempo, el bien debe estar ahora cerca."
print(f"Texto a calcular: {cadena_texto}")
print(f"El total de caracteres es {contar_caracteres(cadena_texto)}")


# 26- Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda num1, num2: num1 % num2
num1 = 10
num2 = 3

resto = resto_division(num1, num2)
print(f"El resto de dividir {num1} entre {num2} es {resto}")

num1 = 11
num2 = 3

resto = resto_division(num1, num2)
print(f"El resto de dividir {num1} entre {num2} es {resto}")


# 27- Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números. Devuelve el valor redondeado a 2 decimales

    Args:
        lista_numeros (list): lista de números

    Returns:
        int: promedio de los números de la lista
    """

    return round(sum(numeros) / len(numeros), 2)

numeros = [500,100,20,3,5,6,9]
promedio = calcular_promedio(numeros)
print(f"Lista de números a calcular: {numeros}")
print(f"El promedio de la lista es de: {promedio}")


# 28- Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def encuentra_primer_duplicado(lista_valores):
    """
    Función que busca y devuelve el primer elemento duplicado en una lista de valores

    Args:
        lista_valores (list): lista de valores

    Returns:
        str: elemento duplicado de la lista
    """
    if not lista_valores:
        return ""

    valor = lista_valores.pop(0)

    if valor in lista_valores:
        return valor
    else:
        return encuentra_primer_duplicado(lista_valores)

lista_valores = [1, "1", 2, "Hola", "Repetido", 4, 5, "Repetido"]
print(f"Lista de valores a buscar: {lista_valores}")

duplicado = encuentra_primer_duplicado(lista_valores)
if duplicado:
    print(f"El valor duplicado es {duplicado}")    
else:
    print(f"La lista no tiene valores duplicados")

lista_valores_1 = ["No", "huye", "el", "que", "se", "retira"]
print(f"Lista de valores a buscar: {lista_valores_1}")
duplicado = encuentra_primer_duplicado(lista_valores_1)
if duplicado:
    print(f"El valor duplicado es {duplicado}")    
else:
    print(f"La lista no tiene valores duplicados")

lista_valores_2 = ["Y", "así", "del", "poco", "dormir", "y", "del", "mucho", "leer", "se", "le", "secó", "el", "cerebro"]
print(f"Lista de valores a buscar: {lista_valores_2}")
duplicado = encuentra_primer_duplicado(lista_valores_2)
if duplicado:
    print(f"El valor duplicado es {duplicado}")    
else:
    print(f"La lista no tiene valores duplicados")


 
# 29- Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.
#Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.
def convierte_a_texto_enmascarado(variable):
    """
    Función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro

    Args:
        variable (str, int, float): variable para convertir a string y enmascarar

    Returns:
        str: texto con las letras enmascaradas a excepción de las 4 últimas
    """
    texto = str(variable)

    if(len(texto) <= 4):
        return texto

    texto_enmascarado = '#' * (len(texto) - 4) + texto[-4:]

    return texto_enmascarado


variable_1 = "Casamientos de parientes tienen mil inconvenientes"
print(f"Variable original: {variable_1}")
print (f"Variable enmascarada: {convierte_a_texto_enmascarado(variable_1)}")

variable_2 = 45666558995
print(f"Variable original: {variable_2}")
print (f"Variable enmascarada: {convierte_a_texto_enmascarado(variable_2)}")

variable_3 = "tres"
print(f"Variable original: {variable_3}")
print (f"Variable enmascarada: {convierte_a_texto_enmascarado(variable_3)}")


# 30- Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def palabras_anagramas(palabra1, palabra2):
    """
    Función que determina si dos palabras son anagramas

    Args:
        palabra1 (str): primera palabra a comparar
        palabra2 (str): segunda palabra a comparar

    Returns:
        str: Devuelve True si son angramas. En caso contrario, devuelve False
    """
    if (sorted(palabra1.lower()) == sorted(palabra2[::-1].lower())):
        return True
    return False

palabra1 = "Hola"
palabra2 = "Caracola"

if palabras_anagramas(palabra1, palabra2):
    print(f"Las palabras {palabra1} y {palabra2} son anagramas")
else:
    print(f"Las palabras {palabra1} y {palabra2} no son anagramas")

palabra1 = "Roma"
palabra2 = "Amor"
if palabras_anagramas(palabra1, palabra2):
    print(f"Las palabras {palabra1} y {palabra2} son anagramas")
else:
    print(f"Las palabras {palabra1} y {palabra2} no son anagramas")

palabra1 = "Seto"
palabra2 = "Esto"
if palabras_anagramas(palabra1, palabra2):
    print(f"Las palabras {palabra1} y {palabra2} son anagramas")
else:
    print(f"Las palabras {palabra1} y {palabra2} no son anagramas")

     
# 31- Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en 
#    la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

# No vamos a tener en cuenta los nombres compuestos

def encuentra_nombre():
    """Función que solicita al usuario introducir:
        1- Una lista de nombres separadas por espacios
        2- Un nombre a buscar en la lista.

    Busca el nombre introducido en la lista. 
    No se van a tener en cuenta los nombres compuestos tipo Jose María. Se van a tratar como dos nombres separados.
       
    Raises:
        ValueError: Devuelve error si el nombre no está en la lista
    """
    lista_nombre = input("Introduce una lista de nombres, separados por un espacio: ").split()
    nombre_a_buscar = input("Introduce el nombre a buscar: ").lower()

    lista_nombre = [nombre.lower() for nombre in lista_nombre]

    if nombre_a_buscar in lista_nombre:
        print(f"Se ha encontrado el nombre {nombre_a_buscar} en la lista {lista_nombre}")
    else:
        raise ValueError(f"El nombre {nombre_a_buscar} no en la lista  {lista_nombre}")

try:
    encuentra_nombre()
except ValueError as e:
        print(e)


# 32- Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto 
#     del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

#Entiendo como puesto del empleado, la posición que ocupa en la lista, contando la primera posición como 1 y no como 0
def encuentra_empleado(lista_empleados, nombre_empleado):
    """
    Función que busca un empleado en la lista de empleados

    Args:
        lista_empleados (list): lista de empleados
        nombre_empleado (str): nombre del empleado a buscar

    Returns:
        int, str: Si se encuentra el empleado en la lista, devuelve un int con el puesto que ocupa en la lista. Sino, devuelve un mensaje indicando que no está en la lista
    """
    lista_empleados = [nombre.lower() for nombre in lista_empleados]
    nombre_empleado = nombre_empleado.lower()

    if nombre_empleado in lista_empleados:
        return lista_empleados.index(nombre_empleado)+1
    
    return f"No se ha encontrado al empleado {nombre_empleado}"
    
lista_empleados = ["Don Quijote", "Sancho Panza", "Dulcinea del Toboso", "Rocinante"]
nombre_empleado = "Sancho Panza"

posicion = encuentra_empleado(lista_empleados, nombre_empleado)

if (type(posicion) == int):
    print (f"El empleado {nombre_empleado} está en el puesto {posicion}")
else:
    print (posicion)


lista_empleados = ["Don Quijote", "Sancho Panza", "Dulcinea del Toboso", "Rocinante"]
nombre_empleado = "Sancho panza"

posicion = encuentra_empleado(lista_empleados, nombre_empleado)
if (type(posicion) == int):
    print (f"El empleado {nombre_empleado} está en el puesto {posicion}")
else:
    print (posicion)

lista_empleados = ["Don Quijote", "Sancho Panza", "Dulcinea del Toboso", "Rocinante"]
nombre_empleado = "Sancho panzo"

posicion = encuentra_empleado(lista_empleados, nombre_empleado)
if (type(posicion) == int):
    print (f"El empleado {nombre_empleado} está en el puesto {posicion}")
else:
    print (posicion)
 
# 33- Crea una función lambda que sume elementos correspondientes de dos listas dadas.
suma_listas = lambda lista1, lista2: [valor_lista1 + valor_lista2 for valor_lista1, valor_lista2 in zip(lista1, lista2)]

lista1 = [2,2,3,4,5]
lista2 = [5,4,3,2,2]

print(f"Valores de la primera lista {lista1}")
print(f"Valores de la segunda lista {lista2}")

print (f"Lista con los valores sumados: {suma_listas(lista1, lista2)}")


# 34- Crea la clase Arbol define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#  crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
#  El objetivo es implementar estos métodos para manipular la estructura del árbol

# 1. Crear un árbol.
arbol = Arbol.Arbol()

# 2. Hacer crecer el tronco del árbol una unidad.
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
# La función nueva_rama podría tener un parámetros indicando el número de ramas a crecer, que por defecto sea 1.
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
arbol.info_arbol()


#36 Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
#   Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo

try:
    alicia = UsuarioBanco.UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco.UsuarioBanco("Bob", 50, True)

    bob.agregar_dinero(20)
    bob.transferir_dinero(80, alicia)
    alicia.retirar_dinero(50)
    alicia.imprimir_saldo()
    bob.imprimir_saldo()
except Excepciones.NoCuentaBancaria as e:
    print(e)
except Excepciones.SinDineroEnBanco  as e:
    print(e)


# 37- Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
# contar_palabras, reemplazar_palabras , eliminar_palabra. 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

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


 

# 38- Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
#     Consideramos noche de 22:00 a 6:59
inicio_noche1 = datetime.strptime("22:00", "%H:%M").time()
fin_noche1 = datetime.strptime("23:59", "%H:%M").time()
inicio_noche2 = datetime.strptime("00:00", "%H:%M").time()
fin_noche2 = datetime.strptime("6:59", "%H:%M").time()

#     Consideramos día de 7:00 a 14:59
inicio_dia = datetime.strptime("07:00", "%H:%M").time()
fin_dia = datetime.strptime("14:59", "%H:%M").time()

#     Consideramos tarde de 15:00 a 21:59
inicio_tarde = datetime.strptime("15:00", "%H:%M").time()
fin_tarde = datetime.strptime("21:59", "%H:%M").time()

try:
    hora_a_calcular = datetime.strptime(input("Introduce la hora del día (formato 24H HH:MM): "), "%H:%M").time()

    if inicio_noche1 <= hora_a_calcular <= fin_noche1 or inicio_noche2 <= hora_a_calcular <= fin_noche2:
        print ("Es de noche")
    elif inicio_dia <= hora_a_calcular <= fin_dia:
        print ("Es de día")
        
    elif inicio_tarde <= hora_a_calcular <= fin_tarde:
        print ("Estamos por la tarde")
    
except ValueError:
    print("Formato de hora no válido")


# 39- Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
#   - 0 - 69 insuficiente
#   - 70 - 79 bien
#   - 80 - 89 muy bien
#   - 90 - 100 excelente
def determina_calificacion():
    """
    Función que calcula la nota en texto a traveés de la calificación que se pide por input

    Raises:
        ValueError: devuelve error si la nota es inferior a 0 o superior a 100.
    """
    nota = int(input("Introduce la nota del alumno: "))

    if 0 <= nota <= 69:
        print ("La calificación es de insuficiente")
    elif 70 <= nota <= 79:
        print ("La calificación es de bien")
    elif 80 <= nota <= 89:
        print ("La calificación es de muy bien")
    elif 90 <= nota <= 100:
        print ("La calificación es de excelente")
    else:
        raise ValueError("La nota debe estar entre 0 y 100")

try:
    determina_calificacion()        
except ValueError as e:
    print (e)


# 40- Escribe una función que tome dos parámetros: 
#     figura (una cadena que puede ser "rectangulo" , "circulo" o  "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcula_area(figura, medidas):
    """
    Función que calcula el area del rectángulo, círculo o triángulo. El tipo de objeto será el primer parámetro y el segundo serán las medidas en un tupla para calcular el area correspondiente.

    Args:
        figura (str): tipo de figura a calcular
        medidas (tuple): Medidas para calcular el área. En el caso del triángulo y rectángulo, serán base y altura. Para el círculo será el radio.

    Raises:
        ValueError: Mostrará error si se pasa una figura diferente a las contempladas.

    
    """
    area = 0

    if figura.lower() == "rectangulo":
    #Área rectángulo= base * altura
        base, altura = medidas
        area = base * altura
        print(f"El area del {figura}, con base {base} y altura {altura} es de {area}")
    elif figura.lower() == "triangulo":
    #Área triángul0 = (base * altura) / 2
        base, altura = medidas
        area = (base * altura) / 2
        print(f"El area del {figura}, con base {base} y altura {altura} es de {area}")
    elif figura.lower() == "circulo":
    #Área círculo = pi*radio2
        radio = medidas[0]
        area = math.pi * radio**2
        print(f"El area del {figura}, con radio {radio} es de {area}")
    else:
        raise ValueError(f"Figura {figura} no contemplada para el cálculo")

figura = "rectangulo"
medidas = (5, 3)
calcula_area(figura, medidas)

figura = "circulo"
medidas = (4, )
calcula_area(figura, medidas)

figura = "triangulo"
medidas = (6, 4)
calcula_area(figura, medidas)
    

#41- En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#    monto final de una compra en una tienda en línea, después de aplicar un descuento. 
#    El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
try:
    precio_articulo = float(input("Introduce el precio original de artículo: "))
    descuento = 0

    tiene_descuento = input("¿Tiene un cupón de descuento?(si / no) ").lower()
    tiene_descuento = tiene_descuento.replace("í", "i")
    
    if tiene_descuento == "si":
        descuento = float(input("Introduce el valor del cupón de descuento: "))

        if 0 < descuento < precio_articulo:
            precio_articulo -= descuento 
        else:
            print("Descuento no válido")

    print(f"El precio final del artículo es de {precio_articulo}")
except ValueError:
    print("Solamente se pueden introducir números")
    