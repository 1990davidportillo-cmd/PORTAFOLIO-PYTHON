frase = "python es genial"

posicion = frase.index("e")
print(f"la letra 'e' esta en la posicion: {posicion}")

posicion_palabra = frase.index("genial")
print(f"la palabra 'genial' comienza en: {posicion_palabra}")

posicion_final = frase.rindex("e")
print(f"la letra 'e' esta en la posicion final: {posicion_final}")