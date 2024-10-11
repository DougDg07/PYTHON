
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
        print("Descarte na lixeira azul.")
        contagem['papel'] += 1
    elif material == 'plástico':
        print("Descarte na lixeira vermelha.")
        contagem['plástico'] += 1
    elif material == 'vidro':
        print("Descarte na lixeira verde.")
        contagem['vidro'] += 1
    elif material == 'metal':
        print("Descarte na lixeira amarela.")
        contagem['metal'] += 1
    elif material == 'orgânico':
        print("Descarte na lixeira marrom.")
        contagem['orgânico'] += 1
    elif material == 'resíduos não recicláveis':
        print("Descarte na lixeira cinza.")
        contagem['não reciclável'] += 1
    else:
        print("Erro! Tente novamente e não contabilizar na contagem de nenhuma lixeira.")

   
    continuar = input("Deseja continuar reciclando? (s/n): ").lower()
    if continuar != 's':
        break

print("\nResumo da reciclagem:")
for material, quantidade in contagem.items():
    print(f"{material.capitalize()}: {quantidade}")

print("Obrigado por contribuir com a reciclagem!")