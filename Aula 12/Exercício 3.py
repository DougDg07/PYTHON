# Após a aventura da aula passada, o aventureiro resolveu treinar mais seu combate; faça uma simulação onde o aventureiro tem uma lista [100, 20], onde 100 é a vida dele e 20 é poder de ataque dele e a cada 7 segundos de treino, ele aumenta o seu poder de ataque com o limite máximo de 30 para o seu poder de ataque

import time

aventureiro = [100, 20]
poder_max = 30
i = 0
print("Aventureiro está começando o treino!")


for i in range(10):  
    time.sleep(2)  
    if aventureiro[1] < poder_max:
        aventureiro[1] += 1
        print(f"Aumentou o poder de ataque! Poder atual: {aventureiro[1]}")
    else:
        print("Poder de ataque já no máximo!")

print(f"Treino finalizado! Vida: {aventureiro[0]}, Poder de Ataque: {aventureiro[1]}")
