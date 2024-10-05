# Faça um program que calcule o IMC do usuário e dê a classificação conforme a tabela na tela:
#Calculo do IMC: IMC = peso/altura*altura
#Coloque também o grau de obesidade

print("Vamos calcular o IMC!")
peso = float(input("Quanto você pesa em kg:"))
altura = float(input("Digite sua altura:"))
imc = int(peso / (altura * altura))


if (imc < 18.5):
    print("Magreza")
    print("grau 0")
elif(imc >= 18.5 and imc <= 24.9):
    print("normal")
    print("grau 0")
elif(imc >= 25 and imc <= 29.9):
    print("sobrepeso")
    print("grau 1")
elif(imc >= 30 and imc <= 39.9):
    print("Obesidade") 
    print("grau 2") 
elif(imc >= 40):
    print("Obesidade Grave")
    print("grau 3")
else:
    ("Valor não declarado")        

print(f"Seu IMC é: {imc}")
