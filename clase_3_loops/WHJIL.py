def ejercicio_4_while():

    acum = 0
    cont = 0
    nota = int(input("Ingrese la nota del alumno: "))

    while nota != 0:

        acum = acum+int(nota)
        cont = cont+1
        nota = int(input("Ingrese la nota del alumno: "))

    if cont == 0:

        print("NO HA INGRESADO NINGUNA NOTA")

    else:
        promedio = int(acum) / int(cont)

        print(f"El promedio de las notas es {promedio}")







ejercicio_4_while()
