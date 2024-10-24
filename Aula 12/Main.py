#main.py
from calculadora import somar, subtrair, multiplicar, dividir

print("Selecione a operação:")
print("1 Somar")
print("2 Subtrair")
print("3 Multiplicar")
print("4 Dividir")

escolha = input("")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = somar(numero1, numero2)
    print(resultado)
elif escolha == '2':
    resultado = subtrair(numero1, numero2)
    print(resultado)
elif escolha == '3':
    resultado = multiplicar(numero1, numero2)
    print(resultado)
elif escolha == '4':
    resultado = dividir(numero1, numero2)
    print(resultado)
else:
    print("Opção inválida.")

#Exemplo0
import random

# Configurações do jogo
tamanho_tabuleiro = 5
navio_linha = random.randint(0, tamanho_tabuleiro - 1)
navio_coluna = random.randint(0, tamanho_tabuleiro - 1)

# Inicializa o tabuleiro
tabuleiro = [["~"] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))