class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: Guau guau!")

    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")

    def descripcion(self):
        return f"{self.nombre} es un perro de {self.edad} años"


# Crear objeto
fido = Perro(nombre="Fido", edad=3)

# Usar métodos
fido.ladrar()
fido.cumplir_anios()
print(fido.descripcion())

fido.cumplir_anios()
fido.cumplir_anios()
fido.cumplir_anios()

print(fido.descripcion())
