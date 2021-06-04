# CRIE UMA LISTA COM 5 CONTATOS

lista_contatos = []

lista=[("Rosicleia","47991177023"),("João","478596455"), ("Manoela", "479962358"), ("Paula", "4799802383"), ("Lola", "47988388")]

for i in lista:
    nome = (i[0])
    numero = (i[1])
    print("Nome: %s\t  Número: %s" % (nome, numero))


print(type(lista))
print(lista[0])
print(lista[0][0])

if "Rosicleia" in lista[0]:
    print("Encontrada!")
else:
    print("Não está na lista!")






