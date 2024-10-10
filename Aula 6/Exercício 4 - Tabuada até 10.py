#Faça um programa que peça 1 número ao cliente e faça sua tabuada (até o 10)

x = 0


numero = int(input("Entre com um número:"))
while x<=10:
    resultado = x * numero
    print(f"{x} x {numero} = {resultado}")
    x += 1        