#Faça um programa para um lava rapido onde:
# 1 - Lavagem Completa a R$50,00
# 2 - Lavagem Básica à R$35,00
# Caso o usuário queira, o pretinho custa mais R$ 5,00
# Retorne o serviço + valor dele
servico = int(input("Bem Vindo ao SenacWash, qual opção de lavagem você gostaria?------\n Digite 1 para Lavagem Completa - R$50,00 \n Digite 2 para Lavagem Básica  - R$ 35,00\n" ))
lavagemCompleta = 50.00
lavagemBásica = 35.00
pretinho = 5.00


if(servico == 1):
    lavagemCompleta = 50
    print(f"Você selecionou a Lavagem Completa \n")
elif(servico == 2):
      lavagemBásica = 35
      print(f"Você selecionou a Lavagem Básica \n")
else:    
    print("Opção invalida, por favor escolha uma opção válida!")

pretinho = input(f"Gostaria de adicionar o pretinho por mais R$ 5,00? (Sim ou Não)").lower
if(pretinho == "sim"):
     valortotal += 5
     print("O serviço de {lavagemCompleta} será !")
     

