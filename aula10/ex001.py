# Exercício 1 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

num  =  0
maior  =  0.3
menor  =  2.3
alunomaior  =  num
alunomenor  =  num

for  cont  in  range( 2 ):
    num  =  int ( input ( "Qual seu número de aluno?" ))

    alt  =  float ( input ( "Qual sua altura?" ))

    if  alt  >  maior :
        maior  =  alt
        alunomaior  =  num

    if  alt  <  menor :
        menor  =  alt
        alunomenor  =  num

print( f'O maior aluno é o que tem o número: { alunomaior } \n Sua altura é: { maior } \n O menor aluno é o que tem o número: { alunomenor }\n Sua altura é: { menor }' )

