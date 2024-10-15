#Utilizando for, faça um programa que peça 5 números ao usuário e no final dê a sua soma.

soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: ")) 
    soma += numero  

print(f"A soma dos números é: {soma}")