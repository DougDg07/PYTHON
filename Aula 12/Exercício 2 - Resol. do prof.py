#Faça um programa que divide o armário de uma escola e permita colocar o nome do aluno responsável/ pagante da gaveta. O armário tem dimensão 5x5

matriz = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
]

#A escola adicionou um novo armário 3x3 perto das salas de aula e o chamou de armário VIP. Caso o aluno adquira uma gaveta no armário comum, custará R$30,00 ao mês o VIP custará R$50,00. Adicione no sistema essa seleção e retorne para o usuário o custo.
    
matriz2 = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

tipo_armario = input("Qual armário você deseja (comum/vip)? ").lower()

if tipo_armario == "comum":
    nome = input("Qual o seu nome? ")
    linha = int(input("Em qual linha do armário comum será a sua gaveta? (0 a 4) "))
    coluna = int(input("Em qual coluna do armário comum será a sua gaveta? (0 a 4) "))

    if matriz[linha][coluna] == "":
        matriz[linha][coluna] = nome
        custo = 30.00
        print(f"Você escolheu o armário comum. O custo mensal é R${custo:.2f}.")
    else:
        print("Essa gaveta já está ocupada! Tente outra.")

    for linha in matriz:
        print(linha)

elif tipo_armario == "vip":
    nome = input("Qual o seu nome? ")
    linha = int(input("Em qual linha do armário VIP será a sua gaveta? (0 a 2) "))
    coluna = int(input("Em qual coluna do armário VIP será a sua gaveta? (0 a 2) "))

    if matriz2[linha][coluna] == "":
        matriz2[linha][coluna] = nome
        custo = 50.00
        print(f"Você escolheu o armário VIP. O custo mensal é R${custo:.2f}.")
    else:
        print("Essa gaveta já está ocupada! Tente outra.")

    for linha in matriz2:
        print(linha)

else:
    print("Tipo de armário inválido! Tente novamente.")