#Faça um programa usando for que peça 4 números e some apenas os 2 números ímpares

soma = 0
for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))
 
    if numero % 2 != 0:
        soma += numero


print(f"A soma dos dois primeiros números ímpares é: {soma}")