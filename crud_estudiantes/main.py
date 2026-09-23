#Punto de entrada del CRUD.

from crud_estudiantes.menu import mostrar_menu
from crud_estudiantes.operaciones import (
    agregar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante,
    mostrar_estudiantes,
)


def ejecutar_crud():
    # Controla el menú principal y conserva el arreglo en memoria.
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_crud()
