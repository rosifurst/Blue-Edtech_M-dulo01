dic1 = {"valor1", "valor2" }
print(type(dic1))

# dicionário
contatos = {"Pedro":["666-555", "Rua tal"]}      # dic = {chave:valor}
            #chave  #conteudo
print(type(contatos))

lista = [("Rosicleia","47991177023"),("João","478596455"), ("Manoela", "479962358"), ("Paula", "4799802383"), ("Lola", "47988388")]

print()

# Criando um dicionário a partir da lista acima com a função dict()

contatos = dict(lista) # dicionario = dic(lista_a_ser_convertida)
print(contatos)

print("Type da lista contatos:")
print(type(contatos))

print("Type da lista")
print(type(lista))

dicionario_contatos = {"Alexandre": "555-444", "Talita":"111-999", "Najda":"444-777"}

print(dicionario_contatos)
print(len(dicionario_contatos))



# acessando um valor dentro de um dicionario

print('Acessando o valor da chave "Rosicleia ')

print(dicionario_contatos.get("Rosicleia"))

print(dicionario_contatos.item("Ana Paula"))

print(dicionario_contatos)

nome = input("Digite o nome:")
print(dicionario_contatos["Rosicleia"])

print(contatos.get(nome,"Nome não encontrado"))

