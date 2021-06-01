filmes = ["Os Vingadores", "Forest Gamp", "A procura da Felicidade", "Como eu era antes de você", "O lobo de Wall Street", "Dois Coelhos", "Up", "Lagoa Azul"]

filmes_novos = ["Histórias Cruzadas", "Esqueceram de mim", "Desventuras em Série " "Poderoso chefão"]

filmes.extend(filmes_novos)


filmes.append(input("Filme:"))

print(filmes)

filmes.sort()
print()
print("Ordenada: \n", filmes)

for i in filmes:
    print(i)

print()

filmes.reverse()

for i in filmes:
    print(i)

filmes.insert(', "Pianista')
filmes.insert(10, "Projeto X")

for filme in filmes:
    print(filme)