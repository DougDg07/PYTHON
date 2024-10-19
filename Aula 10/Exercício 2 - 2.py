import random

numero1 = random.randint(20, 50)
numero2 = random.randint(20, 50)
numero3 = random.randint(20, 50)
numero4 = random.randint(20, 50)


print("Os números gerados são:")
print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"Número 3: {numero3}")
print(f"Número 4: {numero4}")


numeros = [numero1, numero2, numero3, numero4]


numeros.sort(reverse=True)


print("Números ordenados de forma decrescente:")
for i, num in enumerate(numeros, start=1):
    print(f"Número {i}: {num}")
