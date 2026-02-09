palabra = "javascript"

for letra in palabra:
    print(f"letra: {letra}")

texto = "hola mundo"

contador = 0
for caracter in texto:
    if caracter.lower() in "aeiou":
        contador +=1
        print(f"vocal encontrada: {caracter}")

print(f"\nTotal de vocales: {contador}")

nombre = "FIBONACCI"

for i, ketra in enumerate(nombre):
    print(letra*(i+1))