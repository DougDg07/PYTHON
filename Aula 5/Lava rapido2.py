print("Escolha o tipo de lavagem:")
print("1 - Lavagem Completa a R$50,00")
print("2 - Lavagem Básica a R$35,00")

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
escolha = int(input("Digite o número 1 para Lavagem Completa e 2 para Lavagem Básica: "))

if escolha == 1:
    tipo_servico = "Lavagem Completa"
    valor = 50.00
elif escolha == 2:
    tipo_servico = "Lavagem Básica"
    valor = 35.00
else:
    print("Opção inválida.")
    exit()


pretinho = input("Deseja adicionar o pretinho por mais R$5,00? (s/n): ").lower()

if pretinho == "s":
    valor += 5.00
    tipo_servico += " + Pretinho"
else:
    print("Sem problemas, deixamos para próxima vez! =)")

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
print(f"Serviço: {tipo_servico}")
print(f"Valor total: R${valor:.2f}")

