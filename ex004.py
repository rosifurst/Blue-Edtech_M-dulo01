# Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

def voto(ano):
  from datetime import date  # IMPORTANDO A BIBLIOTECA
  atual = date.today().year #ANO ATUAL
  idade = atual - ano # CALCULA IDADE
  if idade < 16:
    return f'Com {idade} anos: NÃO VOTA.' 
  
  elif 16 <= idade < 18 or idade > 65:
    return f'Com {idade} anos: VOTO OPCIONAL.'
  
  else:
    return f'Com {idade} anos: VOTO OBRIGATÓRIO '

# PROGRAMA PRINCIPAL

nasc = int(input("Em que ano você nasceu?"))
print(voto(nasc))