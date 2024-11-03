'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Sara Gancedo-Rodriguez Garcia
- Eduardo Martinez Abós
EJERCICIO: 2
EXPLICACIONES:
Este programa compara las asignaturas aprobadas por dos estudiantes utilizando conjuntos; primero solicita al usuario ingresar las
asignaturas de cada estudiante y las guarda en un conjunto para evitar duplicados. Luego calcula tres resultados distintos usando
operaciones de conjuntos: asignaturas aprobadas por ambos estudiantes mediante el uso de la intersección, asignaturas aprobadas
solo por el primer estudiante mediante diferencia y asignaturas aprobadas por al menos uno de los dos estudiantes mediante la unión: 
finalmente mostrando los resultados al usuario.
'''

def pedir_asignaturas (num_estudiantes):
    asignaturas = set() # Creamos un conjunto para poder almacenar las asignaturas 
    num_asignaturas = int(input(f"Introduce el número de asignaturas aprobadas del alumno {num_estudiantes}:"))
    for i in range (num_asignaturas): # Bucle para añadir al conjunto la asignatura aprobada
        asignatura = input(f"Introduce la asignatura {i+1} aprobada del estudiante {num_estudiantes}:")
        asignaturas.add(asignatura) # Añade la asignatura al conjunto
    return asignaturas # Devuelve las asignaturas aprobadas (introducidas)

def comparar_asignaturas():
    print("Estudiante 1:")
    asignaturas_estudiante1 = pedir_asignaturas(1) # Solicita las asignaturas del primer estudiante
    
    print("\nEstudiante 2:")
    asignaturas_estudiante2 = pedir_asignaturas(2) # Solicita las asignaturas del segundo estudiante
    
    asignaturas_ambos = asignaturas_estudiante1 & asignaturas_estudiante2 # Calcula las asignaturas aprobadas por ambos estudiantes
    print("\nAsignaturas aprobadas por ambos estudiantes:", asignaturas_ambos)
    
    solo_estudiante1 = asignaturas_estudiante1 - asignaturas_estudiante2 # Calcula las asignaturas aprobadas sólo por el primer estudiante
    print("Asignaturas aprobadas solo por el primer estudiante:", solo_estudiante1)
    
    asignaturas_al_menos_uno = asignaturas_estudiante1 | asignaturas_estudiante2 # Calcula las asignaturas aprobadas por al menos uno de los estudiantes
    print("Asignaturas aprobadas por al menos uno de los estudiantes:", asignaturas_al_menos_uno)

comparar_asignaturas()
