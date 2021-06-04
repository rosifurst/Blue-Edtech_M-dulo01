pessoas = {}
lista = []
while True:
    nome = input('Nome: ')
    idade = int(input('idade: '))
    sexo = input('Sexo[M/F]: ').upper()
    pessoas[nome] = [idade, sexo]
    while sexo != 'M' and sexo != 'F':
        print("Sexo inválido")
        print()
        sexo = input('Sexo[M/F]: ').upper()

    if sexo == 'M' or sexo == 'F':

        if sexo == 'F':
            lista += [nome]
        soma = 0
        for value in pessoas.values():
            soma += value[0]

        if input('Quer continuar?:[s/n] ') in 'n':

            break
        else:
            print()
            continue
print('~-'*16)
print(f'Temos: {len(pessoas)} pessoas cadastradas')
print('~-'*16)
media = soma / len(pessoas)
print(f'Média da idade: {media}')
print('~-'*16)
print("====Lista feminina====")
for cont in lista:
    print(cont)
print('~-'*16)
print('====Pessoas acima da média====')
for k, v in pessoas.items():
    if v[0] > media:
        print(f'{k} - {v[0]}')