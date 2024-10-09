#Faça um programa que: pergunte se o usuario quer um combo ou 1 item individual. Onde o Hamburguer, custa $10,00, a Batata frita, custa $10,00, o Refrigerante custa $10,00 e o Combo custa $22,00.
#O cliente pode adicionar 2 itens, mas caso faça, ofereça o 3° item por $2,00, incentivando e vendendo indiretamente o combo e no final imprima seu pedido e seu valor.
preco_hamburguer = 10.00
preco_batata = 10.00
preco_refrigerante = 10.00
preco_combo = 22.00
opcao = int(input("Selecione a opção:\n1 - Hamburguer\n2 - Batata Frita\n3 - Refrigerante\n4 - Combo (R$22,00)\n"))

if opcao == 1:
    pedido = "Hamburguer"
    valor_total = preco_hamburguer
elif opcao == 2:
    pedido = "Batata Frita"
    valor_total = preco_batata
elif opcao == 3:
    pedido = "Refrigerante"
    valor_total = preco_refrigerante
elif opcao == 4:
    pedido = "Combo (Hamburguer, Batata Frita e Refrigerante)"
    valor_total = preco_combo
else:
    print("Opção inválida.")
    exit()

adicionar = input("Deseja adicionar mais um item? (Sim/Não)\n").capitalize()


if adicionar == "Sim" and opcao != 4:
    segundo_item = int(input("Selecione o segundo item:\n1 - Hamburguer\n2 - Batata Frita\n3 - Refrigerante\n"))

    if segundo_item == 1 and opcao != 1:
        pedido += " e Hamburguer"
        valor_total += preco_hamburguer
    elif segundo_item == 2 and opcao != 2:
        pedido += " e Batata Frita"
        valor_total += preco_batata
    elif segundo_item == 3 and opcao != 3:
        pedido += " e Refrigerante"
        valor_total += preco_refrigerante
    else:
        print("Item já selecionado ou inválido.")


if adicionar == "Sim" and opcao != 4 and valor_total == 20.00:
    terceiro_item = input("Adicione o terceiro item por R$2,00? (Sim/Não)\n").capitalize()

    if terceiro_item == "Sim":
        pedido += " + 3º item"
        valor_total += 2.00


print(f"Seu pedido: {pedido}")
print(f"Valor total: R${valor_total:.2f}")