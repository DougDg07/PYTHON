#Faça um programa que receba 1 número e diga se ele é primo ou não

#Peço um número
numero = int(input("Entre com um número:"))

#Uso uma variável de apoio que definirá se um número é primo ou não
primo = True

#Faço um loop que vai do número 2 até o número antecessor a ele
for i in range(2, numero):
    
    #Se um númeor for divisível por qualquer númeor sem ser 1 ou ele mesmo, "primo" será falso
    if (numero % i == 0):
       primo = False

#Se "primo" for falso, é porque ele é divisível por mais algum número sem ser 1 e ele mesmo       
if (primo == False):
    print("Esse número não é primo")
else:
    print("Esse é um número é primo")