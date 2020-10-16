class Notas:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_nota_class(self):

        print(f"{str(self.nombre)}: {float(self.nota)}")

    def mostrar_nota_promocionados(self):

        if float(self.nota) >= 7:
            print(f"{str(self.nombre)}, Su nota {float(self.nota)}")

    def retornar_nota(self):

        nota = float(self.nota)

        return nota
