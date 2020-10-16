from
def opciones_menu():
    print("Ingrese 1 para cargar un empleado")
    print("Ingrese 2 para mostrar la lista de empleados")
    print("Ingrese 3 para buscar un empleado por legajo y mostrar todos sus datos")
    print("Ingrese 4 para buscar un empleado por nombre y asignarle horas trabajadas")
    print("Ingrese 5 para conocer el porcentaje de empleados con un sueldo menor a $30.000")
    print("Ingrese 0 para salir")

    return input("Ingrese una opcion: ")


def menu():

    empleados = []
    opcion = opciones_menu()
    while opcion != 0:

        if opcion == 1:
            empleado = Empleado()0