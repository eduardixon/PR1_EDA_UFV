from collections import deque
#deque permite eliminar elementos desde ambos extremos de una cola

class Cola:
    def __init__(self):
        self.solicitudes = deque() 

    def encolar(self, solicitud):
        self.solicitudes.append(solicitud) 

    def desencolar(self):
        if self.solicitudes:
            return self.solicitudes.popleft() #Quita el elemento más a la izq, en lugar del último como sería con el pop
        else:
            return None

def aceptar_solicitud(amigos, cola):
    solicitud = cola.desencolar()
    if solicitud:
        amigos.add(solicitud) #Para añadir al set() utilizamos la función add
        print(f"Aceptaste la solicitud de '{solicitud}'")
    else:
        print("No tiene solicitudes pendientes.")

def enviar_solicitud(cola, nombre):
    cola.encolar(nombre)
    print(f"Has enviado una solicitud a '{nombre}'")


def menu():
    amigos = set()
    cola = Cola()

    # Ejemplos 
    cola.encolar("Isabel")
    cola.encolar("Pedro")
    cola.encolar("Ana")

    while True:
        print("\n   Menú de una red social:")
        print("1. Enviar solicitud de amistad.")
        print("2. Aceptar solicitud de amistad.")
        print("3. Salir.")
        
        opcion = input("Elige una opción por favor: ")
        
        if opcion == "1":
            nombre = input("¿A qué usuario desea enviarle la solicitud?")
            enviar_solicitud(cola, nombre)
        
        elif opcion == "2":
            aceptar_solicitud(amigos, cola)
        
        elif opcion == "3":
            print("Gracias. Está saliendo.")
            break
        
        else:
            print("Opción incorrecta, pruebélo de nuevo.")

menu()
