
#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


from datetime import datetime
dados = dict()
dados = {}
nome = (input("Nome: "))
dados['nome'] = nome
nasc = int(input("Ano de Nascimento: "))
dados['idade'] =  datetime.now().year - nasc
dados['ctps'] = int(input("Carteira de Trabalho (0 não tem)"))

if dados['ctps'] != 0:
    dados['contratação'] = int(input("Ano de Contratação: "))
    dados['salário'] = float(input("Salário: R$"))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)


for k, v in dados.items():
    print(f' - {k} tem o valor {v}')