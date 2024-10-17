#Jogo do palpite. O sistema dera 1 número aleatório entre 1 e 200. O usuário tem 10 palpites para tentar acertar.
#O sistema sempre dá um feedback dizendo se o " número secreto" é maior e o menor que o palpite do usuário

import random

print("Escolha o nível de dificuldade:")
print("1. Fácil (10 tentativas)")
print("2. Médio (7 tentativas)")
print("3. Difícil (5 tentativas)")

while True:
    escolha = input("Digite o número da dificuldade (1, 2 ou 3): ")
    
    if escolha == '1':
        tentativas = 10
        break
    elif escolha == '2':
        tentativas = 7
        break
    elif escolha == '3':
        tentativas = 5
        break
    else:
        print("Opção inválida.")


    numero_secreto = random.randint(1, 200)

    print("\nBem-vindo ao Jogo do Palpite!")
    print(f"Adivinhe o número entre 1 e 200. Você tem {tentativas} tentativas.")

    for tentativa in range(tentativas):
        palpite = int(input("Insira seu palpite: "))
        
        if palpite < 1 and palpite > 200:
            print("Escolha um número entre 1 e 200.")
           

        if palpite < numero_secreto:
            print("O número secreto é maior.")
        elif palpite > numero_secreto:
            print("O número secreto é menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            break
    else:
        print(f"Você não adivinhou. O número era {numero_secreto}.")
    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar!")
        break