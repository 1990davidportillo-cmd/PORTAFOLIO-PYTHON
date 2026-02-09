class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"{self.nombre} ruido de pokemon general")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")


class Tipo_electrico(Pokemon):
    def hacer_sonido(self):
        print(f"{self.nombre} dice pika pika!")


class Tipo_fuego(Pokemon):
    def hacer_sonido(self):
        print(f"{self.nombre} dice char!")
