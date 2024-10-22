print("Olá Aventureiro! Pronto para iniciar sua jornada?")
inventario = ["Espada", "Poção", "Escudo"]
print("Itens iniciais do seu inventário:", inventario)

# Encontro com o Arco
resposta = input("Você encontra um Arco. Deseja adicioná-lo ao seu inventário? (sim/não): ").lower()
if resposta == "sim":
    item = input("Remova um item do seu inventário para adicionar o Arco: ")
    if item in inventario:
        inventario.remove(item)
        inventario.append("Arco")
        print("Itens em seu inventário:", inventario)
    else:
        print("Item não encontrado na mochila.")

# Encontro com o bandido
print("\nVocê encontra um bandido armado que exige sua poção.")
acao = input("Você deseja (1) Enfrentar o bandido ou (2) Entregar sua poção? ")

if acao == "1":
    if "Espada" in inventario:
        print("Você saca sua espada e enfrenta o bandido! Você vence e segue seu caminho.")
    else:
        print("Você tentou lutar sem a espada e perdeu a batalha. Você morreu!")
elif acao == "2":
    entrega = input("Você entregará a poção 'sem tela' no inventário? (sim/não): ").lower()
    if entrega == "sim":
        print("O bandido fica furioso e você é derrotado. Você morreu!")
    elif "Poção" in inventario:
        inventario.remove("Poção")
        print("Você entregou sua poção ao bandido e seguiu seu caminho.")
    else:
        print("Você não tem mais poções para entregar.")
else:
    print("Opção inválida. O bandido se aproveita da sua hesitação e lhe ataca. Você morreu!")

print("Itens finais em seu inventário:", inventario)
