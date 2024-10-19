#Criando uma lista simples com 3 pokemons
pokemons = ["Pikachu", "Charmander", "Bulbasaur"]

#Exibindo a lista
print("Lista de Pokemons:", pokemons)

#Acessando o primeiro Pokémon da lista
print("Primeiro Pokémon:", pokemons[0])

#Adicionando um novo Pokémon à lista
pokemons.append("squirtle")
print("Lista  de Pokémons após adicionar Squirtle", pokemons)

#Removendo o Pokémon "Charmander" de lista
pokemons.remove("Charmander")
print("Lista  de Pokémons após remover Charmander", pokemons)

#Exibindo o tamanho da lista
print("Número de Pokémons na lista:", len(pokemons))
