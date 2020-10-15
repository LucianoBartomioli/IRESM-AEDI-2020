from IRESM_AEDI_2020.clase_6_clases.clase import alquiler

alquileres = []





def cargar_alquiler():

    marca = input("Ingrese la marca del vehiculo: ")
    modelo = input("Ingrese el modelo: ")
    año = input("Ingrese el año: ")
    precio_x_km = float(input("Ingrese el coste por KM: "))
    seguro_alquiler = float(input("Ingrese el seguro de alquiler: "))
    DNI = input("Ingrese el DNI del arrendatario: ")
    nombre = input("Ingrese el nombre del arrendatario: ")
    km_recorridos = float(input("Ingrese los kilometros recorridos: "))
    alquiler1 = alquiler(marca, modelo, año, precio_x_km, seguro_alquiler, DNI, nombre, km_recorridos)
    alquileres.append(alquiler1)






def menu_opcion():
    print("-------------MENU---------------")
    print("(1) Para cargar un nuevo Alquiler en la lista")
    print("(2) Para mostrar la lista de alquileres ")
    print("(0) Para finalizar")
    opcion = int(input("Ingrese una opcion: "))

    return opcion


def menu():
    opcion = menu_opcion()
    while opcion != 0:
        if opcion == 1:
            cargar_alquiler()

        elif opcion == 2:
            for item in alquileres:

                item.mostrar_alquiler()

        opcion = menu_opcion()







menu()










