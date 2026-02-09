password = ""
while password != "escamoso90":
    password = input("Ingrese su password: ").lower().strip()
    if password == "escamoso90":
        print("password incorrecto. intenta de nuevo!")


print("password correcto! acceso concedido.")