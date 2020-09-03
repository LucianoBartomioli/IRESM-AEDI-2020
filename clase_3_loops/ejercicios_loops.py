
def ejercicio_1_for_en_vector():

    nombres = ["Lucas", "Franco", "Luciano", "Malena", "Jonatan", "Luciano", "Rodrigo", "Maria Sol", "Enzo", "Milena"]

    for nombre in nombres:

        print(nombre)

def ejercicio_2_for_en_vector():
    cont = 0


    nombres = ["Lucas", "Franco", "Luciano", "Malena", "Jonatan", "Luciano", "Rodrigo", "Maria Sol", "Enzo", "Milena"]

    for nombre in nombres:
        cont=cont+1

        print(str(cont) + "° " + (nombre))

def ejercicio_3_for_en_vector():
    nombres = ["Lucas", "Franco", "Luciano", "Malena", "Jonatan", "Luciano", "Rodrigo", "Maria Sol", "Enzo", "Milena"]



    for i in range(4, 10):

        print(nombres[i])

    print(f"El nombre en la posicion 1° es {nombres[1]}")


def ejercicio_4_while():

    acum = 0
    cont = -1
    nota = input("Ingrese la nota del alumno: ")

    while nota != 0:
        nota = int(input("Ingrese la nota del alumno: "))
        acum = acum+nota
        cont = cont+1





    promedio = (acum)/(cont)

    print(f"El promedio de las notas es {promedio}")

ejercicio_4_while()
























