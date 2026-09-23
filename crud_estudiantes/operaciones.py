# Operaciones principales del CRUD.

from crud_estudiantes.validaciones import buscar_estudiante, codigo_existe


def agregar_estudiante(estudiantes):
    # Agrega un estudiante al arreglo.
    codigo = input("Código: ").strip()

    if codigo_existe(estudiantes, codigo):
        print("Ya existe un estudiante con ese código.")
        return

    nombre = input("Nombre: ").strip()
    carrera = input("Carrera: ").strip()
    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "carrera": carrera,
    })
    print("Estudiante agregado correctamente.")


def mostrar_estudiantes(estudiantes):
    # Muestra todos los estudiantes guardados.
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print("\n--- ESTUDIANTES REGISTRADOS ---")
    for posicion, estudiante in enumerate(estudiantes, start=1):
        print(
            f"{posicion}. Código: {estudiante['codigo']} | "
            f"Nombre: {estudiante['nombre']} | "
            f"Carrera: {estudiante['carrera']}"
        )


def actualizar_estudiante(estudiantes):
    # Modifica los datos de un estudiante.
    codigo = input("Código del estudiante a actualizar: ").strip()
    indice = buscar_estudiante(estudiantes, codigo)

    if indice == -1:
        print("No se encontró ese estudiante.")
        return

    estudiantes[indice]["nombre"] = input("Nuevo nombre: ").strip()
    estudiantes[indice]["carrera"] = input("Nueva carrera: ").strip()
    print("Estudiante actualizado correctamente.")


def eliminar_estudiante(estudiantes):
    # Elimina un estudiante del arreglo.
    codigo = input("Código del estudiante a eliminar: ").strip()
    indice = buscar_estudiante(estudiantes, codigo)

    if indice == -1:
        print("No se encontró ese estudiante.")
        return

    estudiantes.pop(indice)
    print("Estudiante eliminado correctamente.")
