"""
Problema 1. Procesamiento de una lista de enteros. 
Crea una función que reciba una lista de enteros por parámetro y devuelva otra
lista, de acuerdo a las siguientes acciones:
1. Eliminar los números negativos de la lista.
2. Eliminar los valores que están repetidos, quedándonos con uno de ellos.
3. Ordenar los números resultantes de menor a mayor
Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4]. 
"""
lista = [4,-1,2,4,3,-5,2]

#Paso 1 Eliminar los números negativos de la lista.
#Opción rápida: lista_pos = [num for num in lista if num>=0]
def procesa_listas(lista):

  lista_pos = []
  for num in lista:
    if num>=0:
      lista_pos.append(num)

  print(f"Lista Original: {lista}")
  print(f"Lista sin negativos: {lista_pos}")

  #Paso 2 Eliminar los valores que están repetidos, quedándonos con uno de ellos.
  lista_unica = []
  for num in lista_pos:
    if num not in lista_unica:
      lista_unica.append(num)

  print(f"Lista sin repeticiones: {lista_unica}")

  #Paso 3 Ordenar los números resultantes de menor a mayor.
  lista_ordenada = sorted(lista_unica)
  print(f"Lista ordenada: {lista_ordenada}")

procesa_listas(lista)