class Empleado:
    def __init__(self, nombre, apellido, dni, legajo, puesto, salario_por_hora, cantidad_hs_trabajadas):
        self.nombre = input("Ingrese el nombre")
        self.apellido = input("Ingrese el apellido")
        self.dni = input("Ingrese el DNI")
        self.legajo = input("Ingrese el N° de legajo")
        self.puesto = input("Ingrese el puesto")
        self.salario_por_hora = float(input("Ingrese el salario p/ hora"))
        self.cantidad_hs_trabajadas = 0


    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Legajo: {self.legajo}")
        print(f"Puesto: {self.puesto}")
        print(f"Salario p/hora: {self.salario_por_hora}")
        print(f"Cantidad de hs trabajadas: {self.cantidad_hs_trabajadas}")
        print(f"Sueldo calculado: ${self.cantidad_hs_trabajadas*self.salario_por_hora}")

    def ingresar_cantidad_de_horas(self, cantidad_hs):
        self.cantidad_hs_trabajadas = cantidad_hs