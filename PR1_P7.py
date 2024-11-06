'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodríguez García
- Eduardo Martínez Abós
EJERCICIO: 7
EXPLICACIONES:
Creamos la clase libro y añadimos los atributos pedidos.
Creamos la funcion obtener autores. Despues creamos una variable aux, para iterar por los nodos. Posteriormente un bucle while, para iterar y añadimos a la clase set, los valores de solo los autores de cada nodo. Utilizando tanto la clase Lista, como la clase Libro.
Hacemos una prueba de funcionalidad. (Hemos añadido dos veces el mismo autor, para demostrar que en un set solo toma el mismo valor una vez).
Creamos la variable lista_libros y añadimos todos los libros dentro de esta, que va a ser el valor que tome el parametro de la funcion. Que sera una lista enlazada foramda por instancias de la clase Libro, por lo que podremos acceder tanto a los atributos y metodos de la clase Libro, como a los de la clase Lista.
Por ultimo imprimos en pantalla.

'''

from PR1_P1 import Nodo, Lista

class Libro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

def obtener_autores(lista_libros):
    autores_unicos = set()
    
    aux = lista_libros.primero
    while aux is not None:
        autores_unicos.add(aux.valor.autor)
        aux = aux.sig
    
    return autores_unicos

# Prueba de funcionalidad
lista_libros = Lista()

libros = [ Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967), 
          Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605), 
          Libro("La Sombra del Viento", "Carlos Ruiz Zafón", 2001), 
          Libro("El Amor en los Tiempos del Cólera", "Gabriel García Márquez", 1985), #Añadimos mismo autor, solo aparecera una vez, ya que la clase set, solo toma una vez cada elemento identico.
          Libro("Ficciones", "Jorge Luis Borges", 1944) ]

for libro in libros:
    lista_libros.insertarDerecha(libro)

print(f"Lista de libros: {lista_libros}")
autores_unicos = obtener_autores(lista_libros)
print(f"Autores unicos: {autores_unicos}")
