EscolhaLanche = int(input("---Bem Vindo ao Maquimeleca, qual opção você gostaria?----\n Digite 1 para Hamburguer - R$10,00 \n Digite 2 para Batata Frita - R$10,00 \n Digite 3 para Refrigerante - R$10,00 \n Digite 4 para Combo (Hamburguer + Batata Frita + Refrigerante) - R$22,00 \n"))

item1 = "Hamburguer"
item2 = "Batata Frita"
item3 = "Refrigerante"
item4 = "Combo"

if EscolhaLanche == 1:
    print(f"Você escolheu {item1}")
    adicionar = int(input("Gostaria de adicionar outro item? Digite 2 para Batata Frita e Digite 3 para Refrigerante \n"))
    
    if adicionar == 2:
        print(f"Você escolheu {item1} e {item2}")
        oferecercombo = input("Gostaria de adicionar o refrigerante por mais R$2,00? (sim/não) ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item2}, totalizando R$20,00")
    
    elif adicionar == 3:
        print(f"Você escolheu {item1} e {item3}")
        oferecercombo = input("Gostaria de adicionar a batata frita por mais R$2,00? (sim/não) ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item3}, totalizando R$20,00")
    
    else:
        print(f"Seu pedido é {item1}, totalizando R$10,00")


elif EscolhaLanche == 2:
    print(f"Você escolheu {item2}")
    adicionar = int(input("Gostaria de adicionar outro item? Digite 1 para Hamburguer e Digite 3 para Refrigerante \n"))
    
    if adicionar == 1:
        print(f"Você escolheu {item2} e {item1}")
        oferecercombo = input("Gostaria de adicionar o refrigerante por mais R$2,00? (sim/não) ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item2}, totalizando R$20,00")
    
    elif adicionar == 3:
        print(f"Você escolheu {item2} e {item3}")
        oferecercombo = input("Gostaria de adicionar o hamburguer por mais R$2,00? (sim/não) ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item2} + {item3}, totalizando R$20,00")
    
    else:
        print(f"Seu pedido é {item2}, totalizando R$10,00")

elif EscolhaLanche == 3:
    print(f"Você escolheu {item3}")
    adicionar = int(input("Gostaria de adicionar outro item? Digite 1 para Hamburguer e Digite 2 para Batata Frita \n"))
    
    if adicionar == 1:
        print(f"Você escolheu {item3} e {item1}")
        oferecercombo = input("Gostaria de adicionar a batata frita por mais R$2,00? (sim/não) ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item3}, totalizando R$20,00")
    
    elif adicionar == 2:
        print(f"Você escolheu {item3} e {item2}")
        oferecercombo = input("Gostaria de adicionar o hamburguer por mais R$2,00? (sim/não) ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item2} + {item3}, totalizando R$20,00")
    
    else:
        print(f"Seu pedido é {item3}, totalizando R$10,00")

elif EscolhaLanche == 4:
    print(f"Você escolheu o combo ({item1}, {item2} e {item3}), totalizando R$22,00")

else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
