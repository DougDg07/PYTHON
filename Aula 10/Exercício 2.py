#Faça um programa que gera 4 números aleatórios entre 20 e 50 e depois os ordena de forma decrescente.

import random

numeros = []

for _ in range(4):
    numero = random.randint(20, 50)
    numeros.append(numero)

print("Números gerados:", numeros)

numeros_ordenados = []
while numeros:
    maior = max(numeros)  
    numeros_ordenados.append(maior)  
    numeros.remove(maior)  

print("Números ordenados de forma decrescente:", numeros_ordenados)