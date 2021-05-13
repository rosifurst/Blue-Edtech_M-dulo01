#DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne 
# NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto,
#  sendo que nesses casos Fevereiro terá 29 dias.


def calendario(date):

  dia = int(date[0:2])
  mes = int(date[3:5])
  ano = int(date[6:10])

  month = [
        '','janeiro', 'fevereiro',
        'março','abril',
        'maio','junho',
        'julho','agosto',
        'setembro', 'outubro',
        'novembro', 'dezembro'
      ]

  # Tratamento de erros
  if (len(date) < 10 or len(date) > 10):
    print('Null')
  elif (date[2] != '/' or date[5] != '/'):
    print('Null')
  elif (mes < 1 or mes > 12):
    print('Null')

  # Ano bissexto
  if (ano % 4 == 0 and ano % 100 !=100 or ano % 400 == 0):
    print(f'{dia} de {month[mes]} de {ano} é uma data bissexta')
  else:
    print(f'{dia} de {month[mes]} de {ano} não é uma data bissexta')

date = input('Escreva uma data no formato (dia/mês/ano): ')

calendario(date)