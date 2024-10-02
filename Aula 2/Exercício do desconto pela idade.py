# Pergunte a idade de uma pessoa. Calcule o desconto dos seguintes produtos: 
# Calça Azul: R$ 120,00 - Jaqueta Verde: R$ 150,00
# Sabedno que  valor do desconto é equivalente a idade. Exemplo: 30 ANOS = 30 REAIS DE DESCONTO

idade = int(input("Diga a sua idade:"))

preco_calca = 120
preco_jaqueta = 150

desconto = idade
preco_calca_desconto = preco_calca - desconto
preco_jaqueta_desconto = preco_jaqueta - desconto

print("Preço da Calça Azul com desconto: R$", preco_calca_desconto)
print("Preço da Jaqueta Verde com desconto: R$", preco_jaqueta_desconto)