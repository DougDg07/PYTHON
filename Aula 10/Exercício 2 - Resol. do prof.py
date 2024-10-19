import random

numero1 = random.randint(20, 50)
numero2 = random.randint(20, 50)
numero3 = random.randint(20, 50)
numero4 = random.randint(20, 50)

print(f"Números gerados: {numero1}, {numero2}, {numero3}, {numero4}")

for i in range(5):
    if numero1 < numero2:
        numero1, numero2 = numero2, numero1
    if numero1 < numero3:
        numero1, numero3 = numero3, numero1
    if numero1 < numero4:
        numero1, numero4 = numero4, numero1    
    if numero2 < numero3:
        numero2, numero3 = numero3, numero2
    if numero2 < numero3:
        numero2, numero3 = numero3, numero2     