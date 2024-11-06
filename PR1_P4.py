'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodríguez García
- Eduardo Martínez Abós
EJERCICIO: 4
EXPLICACIONES:
Primero importamos las clases Nodo y Lista, de esta manera podremos operar sobre ellas.
Despues creamos la funcion nodo medio. 
Primero comprobamos si esta vacia, en caso de que no continuamos.
Creamos dos variables,para poder iterar sobre el valor de los nodos. En caso de que la lista tenga una longitud impar, vamos a usar la variable aux y auxdoble.
La varialbe aux iterar de n en n, mientras que la aux doble de 2n en 2n. De esta manera encontramos el nodo medio cuando acabe el bucle while que iterara por los nodos de la manera explicada anteriormente hasta que auxdoble, llegue a el nodo final de la lista.
De esta manera, mientras auxdoble haya iterado la lista completa, aux habra iterado la mitad.
Si es par, haremos un bucle while que itere hasta la mitad de la lista. Al ser de longitud par, habra dos valores intermedios, y tomara el de mas a la derecha ya que hemos empezado a iterar en el nodo 1, pero le hemos dado a i el valor de 0.
Retornamos el valor de el nodo aux y hacemos pruebas de funcionalidad.

'''

from PR1_P1 import Nodo, Lista

def nodo_medio(self):
    if self.esVacia():
        return "La lista no contiene nignun nodo"
    else: 
        aux = self.primero
        auxdoble = self.primero
        if self.longitud %2 != 0:
            while auxdoble != self.ultimo:
                aux = aux.sig
                auxdoble = auxdoble.sig.sig
        else:
            i = 0
            while i < int(self.len()/2):
                aux =aux.sig
                i += 1  
        return aux.valor

Lista.nodo_medio = nodo_medio
l1 = Lista() #Lista impar
l2 = Lista() #Lista par


l1.insertarIzquierda(9)
l1.insertarIzquierda(8)
l1.insertarIzquierda(7)
l1.insertarIzquierda(6)
l1.insertarIzquierda(5)
l1.insertarIzquierda(4)
l1.insertarIzquierda(3)
l1.insertarIzquierda(2)
l1.insertarIzquierda(1)

l2.insertarIzquierda(10)
l2.insertarIzquierda(9)
l2.insertarIzquierda(8)
l2.insertarIzquierda(7)
l2.insertarIzquierda(6)
l2.insertarIzquierda(5)
l2.insertarIzquierda(4)
l2.insertarIzquierda(3)
l2.insertarIzquierda(2)
l2.insertarIzquierda(1)

print(f"El nodo medio de la lista {l1} es : ", nodo_medio(l1))
print(f"El nodo medio de la lista {l2} es : ", nodo_medio(l2))
