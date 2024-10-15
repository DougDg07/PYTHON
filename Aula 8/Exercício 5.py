# Faça um programa que diga quais dos 20 primeiros multiplos de 5 são pares

numero = 0
for i in range(1, 100):
    numero = i * 5
    if numero % 2 == 0:
        print(i)
    