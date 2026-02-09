import random

def jugar_ahorcado():
    palabras = ["python", "programacion", "computadora", "ahorcado", "clases"]
    palabra_secreta = random.choice(palabras)

    letras_adivinadas = []
    intentos = 6

    print("🎮 Bienvenido al juego del Ahorcado")
    print("La palabra tiene", len(palabra_secreta), "letras")

    while intentos > 0:
        # Mostrar palabra con guiones
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "

        print("\nPalabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        # Verificar si ya ganó
        if "_" not in palabra_mostrada:
            print("🎉 ¡Ganaste! La palabra era:", palabra_secreta)
            break

        letra = input("Ingresa una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("⚠️ Ingresa solo una letra válida")
            continue

        if letra in letras_adivinadas:
            print("⚠️ Ya intentaste esa letra")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            intentos -= 1
            print("❌ Letra incorrecta")

    if intentos == 0:
        print("\n💀 Perdiste. La palabra era:", palabra_secreta)


# Ejecutar el juego
jugar_ahorcado()
