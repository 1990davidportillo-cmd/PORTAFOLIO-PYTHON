edad = input("digite su edad")

if int(edad) >= 5:
    print("puedes entrar al parque")
elif int(edad) <= 5:
    print("eres muy pequeño para entrar")
    print("debes tener al menos 5 años")
else:
    print("ingrese una edad correcta")