def mostrar_persona(**kwargs):
    print("=== INFORMACION ===")
    for clave, valor in kwargs.items():
        return f"{clave}: {valor}"

print(mostrar_persona(nombre="ana",edad=18,ciudad="Antigua Guatemala")
