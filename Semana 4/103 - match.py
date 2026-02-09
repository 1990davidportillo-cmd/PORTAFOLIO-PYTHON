opcion = input("ingresa el dia de la semana: ").lower().lower()

match opcion:
    case "lunes":
        print("A trabajar con las pilas puestas")
    case "martes":
        print("Falta much todavia para el fin de semana")
    case "miercoles":
        print("Ya me estoy cansando faltan energias")
    case "jueves":
        print("Ya casi es viernes")
    case "viernes":
        print("Yuppi ya casi a descansar")
    case "sabado":
        print("Salgo con mi familia")
    case "domingo":
        print("Ya casi es lunes")