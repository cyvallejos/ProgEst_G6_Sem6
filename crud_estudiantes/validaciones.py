#Funciones de búsqueda y validación del arreglo.


def buscar_estudiante(estudiantes, codigo):
    # Devuelve el índice del estudiante o -1 si no existe.
    for indice, estudiante in enumerate(estudiantes):
        if estudiante["codigo"] == codigo:
            return indice
    return -1


def codigo_existe(estudiantes, codigo):
    # Indica si ya existe un código dentro del arreglo.
    return buscar_estudiante(estudiantes, codigo) != -1
