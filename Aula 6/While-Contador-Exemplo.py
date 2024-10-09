soma = 0
contador = 0

#Solicita ao usuario que insira 5 numeros
while contador < 5:
    numero=float(input("insira um numero: "))
    soma += numero
    contador +=1

#Exibe a soma total
print("A soma total é:", soma)