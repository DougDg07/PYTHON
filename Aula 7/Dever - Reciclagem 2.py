print("Bem-vindo ao programa de reciclagem SENAC!")

contagem = {
    'papel': 0,
    'plástico': 0,
    'vidro': 0,
    'metal': 0,
    'orgânico': 0,
    'não reciclável': 0
}

while True:
    material = input("Informe o tipo de material que deseja reciclar (papel, plástico, vidro, metal, orgânico ou resíduos não recicláveis): ").strip().lower()

    if material == 'papel':
        lixeira = "azul"
        contagem['papel'] += 1
    elif material == 'plástico':
        lixeira = "vermelha"
        contagem['plástico'] += 1
    elif material == 'vidro':
        lixeira = "verde"
        contagem['vidro'] += 1
    elif material == 'metal':
        lixeira = "amarela"
        contagem['metal'] += 1
    elif material == 'orgânico':
        lixeira = "marrom"
        contagem['orgânico'] += 1
    elif material == 'resíduos não recicláveis':
        lixeira = "cinza"
        contagem['não reciclável'] += 1
    else:
        print("Erro! Tente novamente e não contabilizar na contagem de nenhuma lixeira.")
        continue  

    resposta = input(f"Em qual lixeira vai o {material}? ").strip().lower()

    if resposta == lixeira:
        print(f"Você acertou! Seu lixo vai na lixeira {lixeira}.")
    else:
        print(f"Você errou! O lixo vai na lixeira {lixeira}. Gostaria de tentar de novo? (s/n): ")
        tentar_novamente = input().strip().lower()
        if tentar_novamente != 's':
            break

    continuar = input("Deseja continuar nosso jogo? (s/n): ").strip().lower()
    if continuar != 's':
        break


print("\nResumo da reciclagem:")
print("Papel:", contagem['papel'])
print("Plástico:", contagem['plástico'])
print("Vidro:", contagem['vidro'])
print("Metal:", contagem['metal'])
print("Orgânico:", contagem['orgânico'])
print("Não reciclável:", contagem['não reciclável'])

print("Obrigado por contribuir com a reciclagem!")
