#CONTINUAÇÃO DO EXERCÍCIO 2
#Enquanto vocÊ segue seu caminho na floresta um bandido armado surge e exige sua poção.
#Você tem a opção de sacar sua espada e enfretar o bandido ou entregar sua poção ao bandido.
#Se tentar lutar contra o bandido sem a espada, você perde a batalha. Se estiver com a espada, você ganha e segue o jogo.
#Se entregar a poção, você fica sem e segue o jogo, mas se disser que irá entregar a poção "sem tela" no inventário, o bandido ficará furioso e será o fim do jogo.
#Caso escolha uma opção inválida o bandido se aproveita da sua hesitação e lhe ataca resultando em fim de jogo. 

#INÍCIO DA AVENT. E ESCOLHA DE ITENS!
print("Olá Aventureiro!! Pronto para iniciar sua Jornada?")
inventario = ["Espada", "Poção", "Escudo"]
print("Itens iniciais do seu inventário:", inventario)

print("Durante sua jornada, você encontra um Arco.")
resposta = input("Você deseja adicionar o Arco em seu inventário? (sim/não): ").lower()

if resposta == "sim":
    print("Você precisa remover um item do seu inventário.")
    item = input("Remova um item do seu inventário: ")
    if item in inventario:
        inventario.remove(item)
        inventario.append("Arco")
        print("Itens em seu inventário:", inventario)
    else:
        print("Item não encontrado na mochila.")

# ENCONTRO COM O BANDIDO!!
print("\nEnquanto você segue seu caminho na floresta, um bandido armado surge e exige sua poção.")
acao = input("Você deseja (1) Enfrentar o bandido com sua espada ou (2) Entregar sua poção? ")

if acao == "1":
    if "Espada" in inventario:
        print("Você saca sua espada e enfrenta o bandido!")
        print("Você vence a batalha e segue seu caminho.")
    else:
        print("Você tentou lutar sem a espada e perdeu a batalha. Você Morreu!")
elif acao == "2":
    entrega = input("Você entregará a poção 'sem tela' no inventário? (sim/não): ").lower()
    if entrega == "sim":
        print("O bandido fica furioso e você é derrotado. Você Morreu!")
    else:
        if "Poção" in inventario:
            inventario.remove("Poção")
            print("Você entregou sua poção ao bandido e seguiu seu caminho.")
        else:
            print("Você não tem mais poções para entregar.")
else:
    print("Opção inválida. O bandido se aproveita da sua hesitação e lhe ataca. Você Morreu!.")

print("Itens finais em seu inventário:", inventario)
