'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Eduaro Martinez Abos
- Sara Gancedo Rodríguez García
EJERCICIO: 1
EXPLICACIONES:
Cremos la clase nodo, le damos como argumento el valor que va a tener ese nodo. Y como argumento el siguiente nodo.
Creamos clase Lista, con los argumentos, primero y lugar (Posicion de los nodos), y la longitud de la lista.
Creamos funcion esVacia, que retornara dos outputs, si esta vaicio el primero y ultimo lugar.
Creamos funcion len, retorna la longitud.

'''
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.longitud = 0

    def esVacia(self): 
        return (self.primero == None) and (self.ultimo == None) # también self.len == 0
    
    def len(self): #me da el tamaño
        return self.longitud

    def insertarIzquierda(self, valor):
        nuevo = Nodo(valor)
        if self.esVacia():
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.sig = self.primero
            self.primero = nuevo
        self.longitud += 1

    def insertarDerecha(self, valor):
        nuevo = Nodo(valor)
        if self.esVacia():
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.sig = nuevo
            self.ultimo = nuevo
        self.longitud += 1

    def insertarPosicion(self, valor, posicion):
        if self.esVacia() or posicion <= 0: # Si la lista es vacía, simplemente insertamos (ignorando la posición). Si la posición es 0 insertamos a la izquierda, lo mismo con valores de posición negativos
            self.insertarIzquierda(valor)
        elif posicion >= self.len():
            self.insertarDerecha(valor)
        else:
            # crear un nuevo nodo
            nuevo = Nodo(valor)
            # buscar el nodo anterior al deseado
            i = 0
            aux = self.primero
            while i < posicion:
                aux = aux.sig
                i += 1
            # arreglar punteros
            nuevo.sig = aux.sig
            aux.sig = nuevo
            # aumentamos el tamaño de la lista con el nuevo nodo
            self.longitud += 1

    def quitarIzquierda(self):
        if not self.esVacia():
            self.primero = self.primero.sig
            self.longitud -= 1
            if self.longitud == 0:
                self.ultimo = None

    def quitarDerecha(self):
        if not self.esVacia():
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                aux = self.primero
                while aux.sig != self.ultimo:
                    aux = aux.sig
                aux.sig = None
                self.ultimo = aux
            self.longitud -= 1

    def quitarPosicion(self, posicion):
        if posicion < 0 or posicion >= self.len():
            raise IndexError("La posición está fuera de los límites de la lista")

        if posicion == 0:
            self.quitarIzquierda()
        else:
            i = 0
            aux = self.primero
            while i < posicion - 1:
                aux = aux.sig
                i += 1
            aux.sig = aux.sig.sig
            if aux.sig == None:
                self.ultimo = aux
            self.longitud -= 1

    def consultarIzquierda(self): # el primero de la lista
        if self.esVacia():
            return None
        return self.primero.valor

    def consultarDerecha(self): # el ultimo de la lista
        if self.esVacia():
            return None
        return self.ultimo.valor

    def consultarPosicion(self, posicion): # el de la posicion de la lista
        if posicion < 0 or posicion >= self.len():
            raise IndexError("La posición está fuera de los límites de la lista")

        aux = self.primero
        for _ in range(posicion):
            aux = aux.sig
        return aux.valor

    # Método sobreescrito para generar un string que represente a la clase
    # ListaEnlazada (lo usa la llamada a print de una ListaEnlazada)
    def __str__(self):
        string = "Head -> "
        aux = self.primero # variable aux para ir recorriendo los nodos
        while aux is not None:
            string += str(aux.valor) + " -> "
            aux = aux.sig
        string += "None"
        return string

# Pruebas básicas de funcionalidad
l1 = Lista()
l2 = Lista()
print(f"¿Es vacía l1? {l1.esVacia()}")

l2.insertarIzquierda(4)
l2.insertarIzquierda(44)
l2.insertarIzquierda(-4)
l2.insertarIzquierda(344)
print(f"¿Es vacía l2? {l2.esVacia()}")

print("Lista l1: ", l1)
print("Lista l2: ", l2)

# Pruebas para la función insertarPosicion
l2.insertarPosicion(2, 0)  # Inserta al principio: 2 -> 344 -> -4 -> 44 -> 4 -> None
print("Después de insertar 2 al principio:", l2)
l2.insertarPosicion(6, 5)  # Inserta al final: 2 -> 344 -> -4 -> 44 -> 4 -> 6 -> None
print("Después de insertar 6 al final:", l2)
l2.insertarPosicion(10, 3)  # Inserta en la posición 3: 2 -> 344 -> -4 -> 10 -> 44 -> 4 -> 6 -> None
print("Después de insertar 10 en la posición 3:", l2)

# Pruebas para la función quitarPosicion
l2.quitarPosicion(0)  # Quita el primer nodo: 344 -> -4 -> 10 -> 44 -> 4 -> 6 -> None
print("Después de quitar la posición 0:", l2)
l2.quitarPosicion(5)  # Quita el último nodo: 344 -> -4 -> 10 -> 44 -> 4 -> None
print("Después de quitar la posición 5:", l2)
l2.quitarPosicion(2)  # Quita el nodo en la posición 2: 344 -> -4 -> 44 -> 4 -> None
print("Después de quitar la posición 2:", l2)
