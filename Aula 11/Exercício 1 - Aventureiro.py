#Você é um aventureiro carregando uma mochila que comporta 3 itens, atualmente ela tem 3 itens: 
#Uma espada, uma poção e um escudo. Ao longo da aventura encontra um Arco no chão e precisa decidir se o coloca na mochila ou não. Caso coloque, precisará descartar outro item a sua escolha.
#Faça um programa simulando essa história e decisão usando lista/vetor

print("Olá Aventureiro!! Pronto para iniciar sua aventura?\n Em seu inventário,você encontrará todos os itens necessários para começar.\n Uma espada, uma poção e um escudo.")
print("Porém, você só pode carregar 3 itens por vez.")
itens = ["Espada", "Poção", "Escudo"]
print("Itens iniciais do seu inventário:", itens)

print("Durante sua Jornada, você encontra um Arco")

resposta1 = input("Você deseja adicionar o Arco em sua mochila? sim/não:").lower()
if resposta1 == "sim":
    print("Ótima escolha! Vamos adicionar o novo item.")
    itens.append(input(f"Adicione o novo item: {itens}"))
    print("Lista  de itens em seu inventário:", itens)

else:
    print("Você está pronto!! Vá começar a caçar uns Dragões!!")
    exit()

itens.remove(input(f"Remova um novo item:{itens}"))
print("Lista  de itens após remover:", itens)

print("Número de itens na lista:", len(itens))    
print("Você está pronto aventureiro, vá matar uns dragões!!")