import random

print(random.randint(1,6))
print(random.random())
print(random.uniform(1.5,2.9999))
numeros = [10,20,30,40,50]
print(random.choice(numeros))
random.shuffle(numeros)
print(numeros)