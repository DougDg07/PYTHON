import random

#Gera um número inteiro aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)
print(f"Número inteiro aleatório entrre 1 e 100: {numero_aleatorio}")

#Em funções passamos parâmetros(números, variáveis). Muitas vezes não temos acesso a lógica por trás. Ela servem para facilitar o desenvolvimento e evitar códigos desnecessários ou "a re-invenção da roda"
#Bibliotecas costumam ter várias funções.

print("Entre com dois números, irei retornar um número aleatório entre eles")
numero_usuario_menor = int(input("Entre com o menor deles"))
numero_usuario_maior = int(input("Entre com o maior deles"))
numero_aleatorio2 = random.randint(numero_usuario_menor,numero_usuario_maior)

print(f"Número inteiro aleatório entre {numero_usuario_menor} e {numero_usuario_maior}: {numero_aleatorio2}")