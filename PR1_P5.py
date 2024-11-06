'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodríguez García
- Eduardo Martínez Abós
EJERCICIO: 5
EXPLICACIONES:
Cuando k sea igual a 0, devolvera el ultimo numero. Devolvera nodo final - k.
Primero comprobamos que no sea una lista vacia.
En nuestra funcion usamos un bucle while para iterar hasta el nodo deseado, que lo encontraremos restando la longitud de la lista y el numero k.
Para imprimir en pantalla, usamos una condicion if, para ver que el k deseado no este fuera de la lista.

'''

from PR1_P1 import Nodo, Lista

def kesimo(self, k):
    if self.esVacia():
        return "La lista no contiene nignun nodo"
    else: 
        aux = self.primero
        i = 1
        while i < int(self.len()- k):
            aux = aux.sig
            i += 1  
        return aux.valor
        pass

Lista.kesimo = kesimo
l3 = Lista() #Lista 


l3.insertarIzquierda(9)
l3.insertarIzquierda(8)
l3.insertarIzquierda(7)
l3.insertarIzquierda(6)
l3.insertarIzquierda(5)
l3.insertarIzquierda(4)
l3.insertarIzquierda(3)
l3.insertarIzquierda(2)
l3.insertarIzquierda(1)


k = int(input("Que valor  k-esimo desde el final de la lista : "))
if l3.len() < k+1:
    print("El valor k introducido, super el tamaño de la lista")    
else:
    print(f"El valor de el nodo k-esimo desde el final de la lista {l3} es : ", kesimo(l3, k))


