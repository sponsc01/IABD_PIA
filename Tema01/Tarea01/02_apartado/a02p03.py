"""
Problema 3. Trabajo con conjuntos
Escribe una función que reciba dos listas de enteros y devuelva un diccionario
con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
CALCULARLOS)
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto,
pero no en ambos).
"""
lista_a = {1,2,3,4,5,6}
lista_b = {5,6,7,8,9,10}

def calcula_diccionarios(lista_a,lista_b):
  print(f"La intersección de ambos conjuntos:{lista_a & lista_b}")
  #o también es posible lista_a.intersection(lista_b)

  print(f"La unión de ambos conjuntos: {lista_a | lista_b}")
    #o también es posible lista_a.union(lista_b)

  print(f"La diferencia simétrica: {lista_a ^ lista_b}")
    #o también es posible lista_a.symmetric_difference(lista_b)

calcula_diccionarios(lista_a,lista_b)