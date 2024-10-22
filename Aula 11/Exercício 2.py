#Refaça o programa usando "if in"

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

print("Você está pronto!! Vá começar a caçar uns Dragões!!")

