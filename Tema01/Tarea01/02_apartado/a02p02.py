import re
import string
"""
Problema 2. Frecuencia de palabras en un texto.
Escribe una función que reciba por parámetro una lista de palabras y la ruta a
un fichero de texto y devuelva un diccionario que muestre cuantas veces
aparecen las distintas palabras de la lista en el fichero de texto. Haz un pequeño
programa que la ponga a prueba.
Requisitos:
1. Eliminar signos de puntuación y convertir todo a minúsculas.
2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra. 
"""
lista = ["coche","skoda","intersección","la"]

#La ruta está definida para abrir el editor de código desde la ruta inicial del repositorio de GitHub
ruta = "Tema01/Tarea01/02_apartado/assets/a02pregunta.txt"

def cuenta_palabras(lista,ruta):

  #Abre el archivo ruta
  #"r" permite la lectura del archivo, entre otras opciones
  #encoding="utf-8" determina la codificación del texto, para evitar problemas con acentos o "ñ"
  with open(ruta,"r",encoding="utf-8") as texto:
    #Lectura de texto
    contenido = texto.read()
    #Una vez obtenido el texto, como ya no se va a volver a usar se cierra.
    texto.close()
    print(f"Texto original \n{contenido}")
    #Apartado 1
    #Se obtienen todos los signos que ya vienen preparados en el módulo string concretamente en punctuation
    #Aparte se escapan los caracteres especiales para que no sean interpretados
    puntuacion = '['+ re.escape(string.punctuation)+']'
    #Ahora ya se eliminan los caracteres que se encuentren en la variable puntuacion
    contenido = re.sub(puntuacion,'',contenido)
    print(f"Texto sin puntuación \n{contenido}")
    #Y se pasa el contenido a minusculas
    contenido = contenido.lower()
    print(f"Texto minusculas \n{contenido}")

    #Apartado 2
    #Se crea el diccionario y se le introducen las palabras seleccionadas anteriormente
    diccionario = {}
    for clave in lista:
      diccionario[clave]=0

    print(f"Diccionario: \n{diccionario}")
    #Se divide el texto en palabras separando por cada espacio
    palabras = contenido.split(' ')
    #Se revisa si la palabra del texto coincide con la del diccionario
    #Si es positivo, se suma 1 a la frecuencia ya establecida
    for parte in palabras:
      if(parte in diccionario):
        diccionario[parte]=diccionario[parte]+1
    #Para rápida comprobación, el resultado del diccionario debe ser el siguiente:
    """
    coche:5
    skoda:2
    intersección:2
    la:3
    """
    print(f"El diccionario queda así tras la iteración: \n{diccionario}")

    #Apartado 3
    #Se usa la función sorted para ordenar, como el input es un diccionario, retorna una lista de tuplas y ordena por el primer elemento de cada tupla.
    #Se necesita dict() para que vuelva a ser un diccionario
    diccionario = dict(sorted(diccionario.items()))
    print("El diccionario ordenado por palabras:")
    for key in diccionario.keys():
      print(f"{key} - {diccionario[key]}")
      

cuenta_palabras(lista,ruta)