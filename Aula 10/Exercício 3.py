#Inicie uma lista dessa forma: 
#Lista: [40, 58, 62, 30] e ordene ela de forma crecente inicie outra lista com os valores.
#Lista 2: [60, 73, 28, 11] e ordene de forma decresente.

lista1 = [40, 58, 62, 30]
lista2 = [60, 73, 28, 11]

lista1.sort()

lista2.sort(reverse=True)

# Exibe os resultados
print("Lista 1 (ordenada de forma crescente):", lista1)
print("Lista 2 (ordenada de forma decrescente):", lista2)
