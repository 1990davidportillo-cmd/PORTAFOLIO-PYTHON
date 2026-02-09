numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)

nombres = ["ana","carlos","maria","pedro"]
for nombre in nombres:
    print(f"hola {nombre}!")

precios = [100,250,75,300,150]

for precio in precios:
    descuento = precio * 0.10
    precio_final = precio + descuento
    print(f"precio: Q{precio} - Descuento: {descuento}")