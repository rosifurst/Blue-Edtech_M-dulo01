# Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: ')) # lerei um str ao inves de int, pq se eu ñ fornecer o input ele retorna um erro.
if g.isnumeric(): #transformo o n_gols em int.
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
