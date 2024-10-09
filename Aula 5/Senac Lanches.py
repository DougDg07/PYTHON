#Faça um programa que: pergunte se o usuario quer um combo ou 1 item individual. Onde o Hamburguer, custa $10,00, a Batata frita, custa $10,00, o Refrigerante custa $10,00 e o Combo custa $22,00.
#O cliente pode adicionar 2 itens, mas caso faça, ofereça o 3° item por $2,00, incentivando e vendendo indiretamente o combo e no final imprima seu pedido e seu valor.
opcao = int(input("Selecione o opcao que gostaria! \n Digite 1 para Hamburguer \n Digite 2 para Batata frita \n Digite 3 para Refrigerante \n Digite 4 para o nosso Combo \n"))


if(opcao == 1):
    lanche ="Hamburguer"
elif(opcao == 2):
     lanche ="Batata frita"
elif(opcao == 3):
    lanche = "Refrigerante"
elif(opcao == 4):
    lanche = "Combo"
else:
    lanche = "Opção invalida"

print(f"A classe que você selecionou é {lanche}.\n")

adicionar = input("Gostaria de adicionar mais algum item? (Sim/Não)\n")

if adicionar == "Sim":
    print("Perfeito, qual item gostaria de adicionar? Digite 2 para Batata frita e 3 para Refrigerante")
    if(adicionar == 2):
        print(f"Você selecionou {lanche} e {lanche}")
        
else:
    print("Sem problemas! Aproveite seu lanche!")