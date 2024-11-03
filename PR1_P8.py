'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodríguez García
- Eduardo Martínez Abós
EJERCICIO: 8
EXPLICACIONES:
Este código implementa un sistema de gestión de amistades en una red social utilizando la clase Usuario para representar
a cada miembro de la red social. Cada Usuario, cuenta con un conjunto llamado amigos donde se almacenan los nombres de
los usuarios con los que establece una relación (amigos) a través de la plataforma, y con una cola de solicitudes que
gestiona las solicitudes pendientes.
Para enviar una solicitud, se utiliza la función enviar_solicitud, la cual verifica que el nombre no se encuentre ya en
la lista de solicitudes, si no esta, entonces se añade y de lo controrario indica que la solicitud ya había sido realizada 
con anterioridad. 
A la hora de desear aceptar una solicitud, se utiliza la funcion aceptar_solicitud, que extrae el primer nombre de la lista 
de solicitudes, eliminando al solicitante de la cola y añadiendo su usuario al conjunto de amigos, y de lo contrario si no 
se encuentran solicitudes, se informará al usuario.
El método incluido en el menú de mostrar_amigos muestra los nombres de los amigos del usuario, y si no se encuentra el usuario 
no tendrá amigos. Asimismo, la función mostrar_solicitudes permite ver las solicitudes pendientes. 
Finalmente, la función menú permite crear un nuevo usuario, enviar y aceptar solicitudes, y consultar las listas de amigos o
de solicitudes pendientes.
'''

from collections import deque

class Usuario:
    def __init__(self, nombre):
        # Inicializa un usuario con un nombre, un conjunto para amigos y una cola para las solicitudes de amistad
        self.nombre = nombre
        self.amigos = set()  # Crea el conjunto de amigos
        self.solicitudes = deque()  # Crea la cola de solicitudes

    def enviar_solicitud(self, destinatario):
        # Envía una solicitud de amistad al destinatario si no hay una solicitud pendiente
        if self.nombre not in destinatario.solicitudes:
            destinatario.solicitudes.append(self.nombre)  # Encolar la solicitud
            print(f"Solicitud enviada de '{self.nombre}' a '{destinatario.nombre}'.")
        else:
            print(f"{self.nombre} ya ha enviado una solicitud a {destinatario.nombre}.")

    def aceptar_solicitud(self, usuarios):
        # Acepta la solicitud de amistad más antigua en la cola de solicitudes
        if self.solicitudes:
            solicitante_nombre = self.solicitudes.popleft()  # Desencolar la solicitud
            solicitante = usuarios[solicitante_nombre]
            self.amigos.add(solicitante_nombre)  # Añadir al solicitante a los amigos
            solicitante.amigos.add(self.nombre)  # Añadir al usuario actual a los amigos del solicitante
            print(f"'{solicitante_nombre}' ahora es amigo de '{self.nombre}'.")
        else:
            print("No hay solicitudes de amistad pendientes.")

    def mostrar_amigos(self):
        # Muestra la lista de amigos del usuario o indica que no tiene amigos
        if self.amigos:
            print(f"Amigos de '{self.nombre}': {self.amigos}")
        else:
            print(f"Amigos de '{self.nombre}': Sin amigos")

    def mostrar_solicitudes(self):
        # Muestra la lista de solicitudes pendientes o indica que no hay solicitudes
        if self.solicitudes:
            print(f"Solicitudes de amistad pendientes para '{self.nombre}': {list(self.solicitudes)}")
        else:
            print("No hay solicitudes pendientes.")

def menu():
    # Función principal que muestra un menú para gestionar usuarios y sus solicitudes de amistad
    usuarios = {}  # Diccionario para almacenar los usuarios por su nombre

    while True:
        # Muestra el menú y solicita una opción al usuario
        print("\nMenú:")
        print("     1. Crear un nuevo usuario")
        print("     2. Enviar solicitud de amistad")
        print("     3. Aceptar solicitud de amistad")
        print("     4. Mostrar amigos")
        print("     5. Mostrar solicitudes de amistad pendientes")
        print("     6. Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == "1":
            # Crea un nuevo usuario si el nombre no existe ya en el sistema
            nombre = input("Introduce el nombre del nuevo usuario: ")
            if nombre not in usuarios:
                usuarios[nombre] = Usuario(nombre)
                print(f"Usuario '{nombre}' creado exitosamente.")
            else:
                print("Ese nombre de usuario ya existe. Intenta con otro nombre.")

        elif eleccion == "2":
            # Enviar una solicitud de amistad de un usuario a otro
            solicitante = input("Introduce el nombre del usuario que envía la solicitud: ")
            destinatario = input("Introduce el nombre del usuario que recibirá la solicitud: ")
            if solicitante in usuarios and destinatario in usuarios:
                usuarios[solicitante].enviar_solicitud(usuarios[destinatario])
            else:
                print("Uno o ambos usuarios no existen. Asegúrate de crearlos primero.")

        elif eleccion == "3":
            # Aceptar la solicitud de amistad para un usuario dado
            nombre = input("Introduce el nombre del usuario que acepta la solicitud: ")
            if nombre in usuarios:
                usuarios[nombre].aceptar_solicitud(usuarios)
            else:
                print("El usuario no existe.")

        elif eleccion == "4":
            # Mostrar amigos de un usuario específico
            nombre = input("Introduce el nombre del usuario: ")
            if nombre in usuarios:
                usuarios[nombre].mostrar_amigos()
            else:
                print("Ese usuario no existe.")

        elif eleccion == "5":
            # Mostrar solicitudes de amistad pendientes de un usuario específico
            nombre = input("Introduce el nombre del usuario: ")
            if nombre in usuarios:
                usuarios[nombre].mostrar_solicitudes()
            else:
                print("Ese usuario no existe.")

        elif eleccion == "6":
            print("Ha salido del sistema.")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 6.")

menu()
