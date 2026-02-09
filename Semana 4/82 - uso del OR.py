dia = input("¿que dia es hoy").upper().strip()

if dia == "SABADO" or dia == "DOMINGO":
    print("es fin de semana")
    print("puedes descansar")

else:
    print("es dia laboral")
    print("a tranajar")