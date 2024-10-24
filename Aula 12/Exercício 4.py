#O aventureiro encontrou outro assaltante no caminho, mas agora que ele está mais treinado, imediatemente foi para o combate!
#Sabendo que cada personagem tem uma quantidade inicial de "Vida" e um valor de "Ataque". seguindo a seguinte estrutura:

#A batalha segue as seguintes regras:

#O aventureiro e o assaltante atacam simultaneamente, causando dano um ao outro com o valor de "Ataque".
#A batalha continua até que a "Vida" de um dos personagens chegue a zero ou abaixo.
#Após cada rodada de ataque, o status de cada personagem (seus valores de "Vida" e "Ataque") deve ser exibido.
#Haverá um intervalo de 4 segundos entre as rodadas de ataque para simular a pausa entre os golpes.
#Ao final da batalha, o loop deve parar e os valores finais de "Vida" de ambos os personagens devem ser mostrados.

#Escreva o código para simular essa batalha e exiba o status de ambos os personagens a cada rodada de ataque.

#Exercicio de treinamento do aventureiro:
import time


aventureiro = [
    ["Vida", "Ataque"],
    [100, 20]
]
assaltante = [
    ["Vida", "Ataque"],
    [60, 20]
]

print("Status inicial:")
for linha in aventureiro:
    print(linha)
for linha in assaltante:
    print(linha)


print("\nA batalha começou!")

while aventureiro[1][0] > 0 and assaltante[1][0] > 0:
    
    aventureiro[1][0] -= assaltante[1][1]  
    assaltante[1][0] -= aventureiro[1][1]  

    
    print("\nStatus após a rodada de ataque:")
    print(f"Aventureiro - Vida: {aventureiro[1][0]}, Ataque: {aventureiro[1][1]}")
    print(f"Assaltante - Vida: {assaltante[1][0]}, Ataque: {assaltante[1][1]}")
    
    time.sleep(4)

print("\nBatalha finalizada!")
print(f"Aventureiro - Vida final: {aventureiro[1][0]}")
print(f"Assaltante - Vida final: {assaltante[1][0]}")
