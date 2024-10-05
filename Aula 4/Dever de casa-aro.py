# Solicita o tamanho do aro da roda
aro = float(input("Digite o tamanho do aro da roda da bicicleta: "))
    
# Calcula os tamanhos recomendados
guidao = aro / 2
manete = aro / 4
quadro = aro  # O tamanho do quadro é igual ao tamanho do aro
   
# Exibe as recomendações
print(f"Recomendações baseadas no tamanho do aro de {aro}:")
print(f"Tamanho do guidão: {guidao:.2f}")
print(f"Tamanho da manete: {manete:.2f}")
print(f"Tamanho do quadro: {quadro:.2f}")