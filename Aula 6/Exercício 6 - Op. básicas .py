#Faça um programa que peça dois número e faça uma operação com base nos seguintes menus:
# 1 - Soma os dois números
# 2 - Subtrai os dois números
# 3 - multiplica os dois números
# 4 - Dividi os dois números

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada (1/2/3/4): ")

if opcao == '1':
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")
elif opcao == '2':
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} é: {resultado}")
elif opcao == '3':
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} é: {resultado}")
elif opcao == '4':
    if num2 != 0:  
        resultado = num1 / num2
        print(f"A divisão de {num1} por {num2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Opção inválida. Por favor, escolha uma operação válida.")