def nombres_alumnos():

    alumnos = []

    for i in range(1, 11):

        alumno = input(f"Ingrese el nombre del  alumno N°{i}:  ")
        alumnos.append(alumno)
    print(alumnos)

def ejercicio_2_modificar_lista():
    frutas = ['manzana', 'peras', 'durazno']
    verduras = ['acelga', 'lechuga']
    nueva_fruta = input("Ingrese una nueva fruta:  ")
    frutas.insert(1, nueva_fruta)
    print(frutas)

    verduras.extend(frutas)
    print(verduras)
    verduras.remove(nueva_fruta)
    print(verduras)
    frutas.pop(-1)
    print(frutas)



def ejercicio_3_ordenar_y_buscar_lista():
    frutas = [1998, 1989, 1970, 2020, 1990]
    print(frutas)
    frutas.sort()
    print(frutas)
    año = int(input("Ingrese el año que desea comprobar que esta en la lista:  "))
    año_search = any(a == año for a in frutas)
    if año_search == 1:
        print("El año ingresado SI se encuentra en la lista")

    else:
        print("El año ingresado NO se encuentra en la lista")
    print(f"El año 1989 se encuentra en el indice {frutas.index(1989)}")

def ejercicio_4_dicionarios():
    jugador = {'comida': 15, 'energia': 100, 'enemigos': 3}
    print(jugador)
    print(jugador.keys())
    nuevas_armas = {'rocas': 4, 'flechas': 5}
    jugador.update(nuevas_armas)
    print(jugador)
    jugador.update({"amigos": 1})
    print(jugador)
    jugador["comida"] = 30
    print(jugador)
    print(f"El jugador tiene {jugador.get('energia')} de energia")




