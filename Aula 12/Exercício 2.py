#Faça um programa que divide o armário de uma escola e permita colocar o nome do aluno responsável/ pagante da gaveta. O armário tem dimensão 5x5

# Definindo o tamanho do armário
linhas = 5
colunas = 5

# Criando o armário como uma lista de listas
armario = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
]

def mostrar_armario():
    print("Armário:")
    for i in range(linhas):
        for j in range(colunas):
            if armario[i][j] == '':
                print(f'[{i},{j}] - Vazio', end='  ')
            else:
                print(f'[{i},{j}] - {armario[i][j]}', end='  ')
        print()
    print()

def adicionar_aluno(linha, coluna, nome):
    if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas:
        print("Posição inválida! Tente novamente.")
        return
    if armario[linha][coluna] != '':
        print("Essa gaveta já está ocupada! Tente outra.")
        return
    armario[linha][coluna] = nome
    print(f"{nome} adicionado à gaveta [{linha},{coluna}].\n")

def main():
    while True:
        mostrar_armario()
        acao = input("Deseja adicionar um aluno (a), sair (s) ou mostrar armário (m)? ").lower()
        
        if acao == 'a':
            try:
                linha = int(input("Digite o número da linha (0-4): "))
                coluna = int(input("Digite o número da coluna (0-4): "))
                nome = input("Digite o nome do aluno: ")
                adicionar_aluno(linha, coluna, nome)
            except ValueError:
                print("Por favor, insira números válidos para linha e coluna.")
        
        elif acao == 's':
            print("Saindo do programa...")
            break
        
        elif acao == 'm':
            mostrar_armario()
        
        else:
            print("Ação inválida! Tente novamente.")

if __name__ == "__main__":
    main()
