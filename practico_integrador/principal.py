from IRESM_AEDI_2020.practico_integrador.metodos import notas

alumnos_notas = []


def cargar_nota():
    nombre = (input("Ingrese el nombre del alumno: "))
    nota = (input("Ingrese la nota del alumno: "))
    nota1 = notas(nombre, nota)
    alumnos_notas.append(nota1)


def mostrar_nota():
    for item in alumnos_notas:
        item.mostrar_nota_class()


def mostrar_nota_promocionados():
    print("Alumnos promocionados: ")
    for nota in alumnos_notas:

        nota.mostrar_nota_promocionados()


def porcentaje_alumnos():

    cont = 0
    cont_reprobados = 0
    cont_regulares = 0
    cont_promocionados = 0
    porcentaje_promocionados = 0
    porcentaje_regulares = 0
    porcentaje_reprobados = 0

    for alumno in alumnos_notas:

        cont = 1 + cont

        if alumno.retornar_nota() < 4:
            cont_reprobados = cont_reprobados + 1

        elif 4 <= alumno.retornar_nota() < 7:
            cont_regulares = cont_regulares + 1

        else:
            cont_promocionados = cont_promocionados + 1

        porcentaje_promocionados = cont_promocionados * 100 / cont
        porcentaje_regulares = cont_regulares * 100 / cont
        porcentaje_reprobados = cont_reprobados * 100 / cont

    print(f"PORCENTAJE DE ALUMNOS REPROBADOS:  %{porcentaje_reprobados}")
    print(f"PORCENTAJE DE ALUMNOS REGULARES %{porcentaje_regulares}")
    print(f"PORCENTAJE DE ALUMNOS PROMOCIONADOS %{porcentaje_promocionados}")


def alumnos_abanderados():
    abanderados = {}

    print("Ingrese el nombre y la nota de los 3 alumnos abanderados: ")
    indice = 0

    for alumno in range(0, 3):
        indice = indice + 1
        print(f"Alumno N°{indice}")
        nombre = str(input("Nombre: "))
        nota = float(input("Nota: "))
        alumnos = {str(nombre): float(nota)}
        abanderados.update(alumnos)

    print(f"Alumnos abanderados {abanderados.items()}")


def opcion_menu():

    print("----------MENU----------")
    print("INGRESE: ")
    print("(1) PARA CARGAR UNA NOTA")
    print("(2) PARA MOSTRAR EL LISTADO DE NOTAS")
    print("(3) PARA MOSTRAR LISTADO DE ALUMNOS PROMOCIONADOS")
    print("(4) PARA MOSTRAR PROCENTAJE DE ALUMNOS REPROBADOS, REGULARES Y PROMOCIONADOS")
    print("(5) PARA CARGAR 3 ALUMNOS ABANDERADOS")
    print("(0) PARA SALIR")

    opcion = int(input("Ingrese una opción: "))
    return opcion


def menu():

    opcion = opcion_menu()
    while opcion != 0:
        if opcion == 1:
            cargar_nota()

        elif opcion == 2:
            mostrar_nota()

        elif opcion == 3:
            mostrar_nota_promocionados()

        elif opcion == 4:
            porcentaje_alumnos()

        elif opcion == 5:
            alumnos_abanderados()

        opcion = opcion_menu()


menu()
