# Faça um programa que diga quais dos 20 primeiros multiplos de 5 são pares e some os ímpares e mostre essa soma no final
soma = 0
for i in range(5, 101, 5):
    if i % 2 == 0:
        print(f"multiplos de 5:{i}")
    
    if i % 2 != 0:
        soma += i
       
print(f"A soma dos ímpares vai dar:{soma}")