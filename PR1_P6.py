'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodríguez García
- Eduardo Martínez Abós
EJERCICIO: 6
EXPLICACIONES:
Creamos la funcion fusionar lista ordenadas, y creamos una nueva lista y dos variables, que van a servir para recorrer los nodos.
Creamos un bucle while en el que vamos a comparar los valores de las lista ordenadas, importante recalcar que este codigo solo servira si las listas que usamos de entrada estan ordeandas.
En el primer bucle, comparamos el valor de la primera lista con el de la segunda, en caso de que el primer valor sea igual o menor lo insertamos en la lista por la parte derecha, para que mantengan el mismo orden y direccion. Luego iteramos al siguiente nodo.
Despues usamos un else, en caso de que el segundo valor sea menor e iteramos al siguiente nodo, añadiendo el valor.
Usarmos dos bucles while, en caso de que haya algun error y no se hayan añadido. Esto puede ayudar en caso de que las dos listas no sean del mismo tamaño, o excepcionalmente en caso de errores.
Por ultimo imprimos y hacemos pruebas de funcionalidad.

'''

from PR1_P1 import Nodo, Lista

def fusionar_listas_ordenadas(lista1, lista2):
    nueva_lista = Lista()
    
    actual1 = lista1.primero
    actual2 = lista2.primero

    while actual1 is not None and actual2 is not None:
        if actual1.valor <= actual2.valor:
            nueva_lista.insertarDerecha(actual1.valor)
            actual1 = actual1.sig
        else:
            nueva_lista.insertarDerecha(actual2.valor)
            actual2 = actual2.sig

    # Si quedan elementos en lista1
    while actual1 is not None:
        nueva_lista.insertarDerecha(actual1.valor)
        actual1 = actual1.sig

    # Si quedan elementos en lista2
    while actual2 is not None:
        nueva_lista.insertarDerecha(actual2.valor)
        actual2 = actual2.sig

    return nueva_lista

# Prueba de funcionalidad
lista1 = Lista()
lista2 = Lista()

valores1 = [1, 3, 5, 7]
valores2 = [2, 4, 6, 8]

for valor in valores1:
    lista1.insertarDerecha(valor)

for valor in valores2:
    lista2.insertarDerecha(valor)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

lista_fusionada = fusionar_listas_ordenadas(lista1, lista2)
print(f"Lista fusionada y ordenada: {lista_fusionada}")
