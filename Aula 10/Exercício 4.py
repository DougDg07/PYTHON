#Faça um programa onde o pikachu começa com uma lista de 4 poderes.
#poderes = ["Choque do Trovão", "Calda de Ferro", "Ataque Rápido", "Esquiva"]
#Faça um programa que você ao adicionar um novo poder, precisa remover outro. Ou seja, o Pikachu precisa ter sempre apenas 4 poderes.

poderes = ["Choque do Trovão", "Calda de Ferro", "Ataque Rápido", "Esquiva"]
print("Poderes iniciais do Pikachu:", poderes)

poderes.append(input(f"Adicione um novo poder: {poderes}")).upper()
print("Lista  de Poderes após adicionar:", poderes)

poderes.remove(input(f"Remova um novo poder:{poderes}")).upper()
print("Lista  de Poderes após remover:", poderes)

print("Número de Poderes na lista:", len(poderes))