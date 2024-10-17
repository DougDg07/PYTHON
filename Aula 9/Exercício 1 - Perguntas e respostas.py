
while True:
    contagem = 0

    resposta1 = input("A linguagem Python é orientada a objeto? (sim/não) ").lower()
    if resposta1 == "sim":
        print("Boooa!! Você acertou!!")
        contagem += 1
    else:
        print("Não não não... Seu burro, vai estudar!!!")

    resposta2 = input("Python permite herança, polimorfismo e encapsulamento? (sim/não) ").lower()
    if resposta2 == "sim":
        print("ISSSAAAEEE MEU GAROUUTO(A)!!")
        contagem += 1
    else:
        print("TEM CERTEZA QUE ESTÁ NO CURSO CERTO???!!!")

    resposta3 = input("Uma lista pode ser alterada após sua criação? (sim/não) ").lower()
    if resposta3 == "sim":
        print("TU É BOM MERRRMO!!")
        contagem += 1
    else:
        print("DESISTO DE TU, VAI VENDER ARTE NA PRAIA!!!")

    continuar = input("Gostaria de jogar novamente? (s/n): ").lower()
    if continuar != "s":
        break

# Exibe a contagem de respostas
print(f"\nContagem de respostas:{contagem}")

if contagem >= 2:
    print("Parabéns! Você é o vencedor!")
else:
    print("Que pena! Tente novamente para ser o vencedor!")