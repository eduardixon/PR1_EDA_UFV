'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodríguez García
- Eduardo Martínez Abós
EJERCICIO: 3
EXPLICACIONES:
Hemos creado una función llamada invertir_cadena la cual recibe una cadena de caracteres del usuario, apilando cada carácter de la cadena, para luego, una vez 
almacenada, desapilar cada carácter para formar la cadena invertida. Se utiliza un ciclo for para ir carácter a carácter en la cadena e ir añadiéndolo a la pila,
y posteriormente, el bucle while para recorrer la pila desapilando carácter a carácter para construir la cadena invertida. 
'''

def invertir_cadena(cadena):
    pila = []  # Creamos la pila vacía

    for caracter in cadena: # Apila cada carácter en la pila
        pila.append(caracter)

    cadena_invertida = ''  # Inicializa cadena invertida
    while pila: #Desapila cada carácter para así construir la cadena invertida
        cadena_invertida += pila.pop()

    return cadena_invertida # Devuelve la cadena invertida 

cadena = input("Introduce una cadena de texto: ") # Pide al usuario que introduzca la cadena deseada
print("Cadena invertida:", invertir_cadena(cadena))
