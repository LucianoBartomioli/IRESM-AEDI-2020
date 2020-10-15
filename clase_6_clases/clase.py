class alquiler:

    def __init__(self, marca, modelo, año, precio_x_km, seguro_alquiler, DNI, nombre, km_recorridos):

        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_x_km = precio_x_km
        self.seguro_alquiler = seguro_alquiler
        self.DNI = DNI
        self.nombre = nombre
        self.km_recorridos = km_recorridos

    def mostrar_alquiler(self):

        print(f"La marca es {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Año {self.año}")
        print(f"Precio por Km ${self.precio_x_km}")
        print(f"Precio del seguro ${self.seguro_alquiler}")
        print(f"DNI del arrendatario {self.DNI}")
        print(f"Nombre {self.nombre}")
        print(f"Km recorridos {self.km_recorridos}")
        print(f"Monto total {self.km_recorridos*self.precio_x_km+self.seguro_alquiler}")







