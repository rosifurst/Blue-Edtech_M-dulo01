#Exercício 3 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
# •	1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#•	5 - Voto Nulo
#•	6 - Voto em Branco
#Faça um programa que calcule e mostre:
##•	O total de votos para cada candidato;
#•	O total de votos nulos;
#•	O total de votos em branco;
#•	A percentagem de votos nulos sobre o total de votos;
#•	A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print ( "[1] - Joao \ n " ,
      "[2] - Maria \ n " ,
      "[3] - Leonardo \ n " ,
      "[4] - Gabriel \ n " ,
      "[5] - Voto Nulo \ n " ,
      "[6] - Voto em Branco" )

voto  =  1
Joao  =  0
Maria  =  0
Leonardo  =  0
Gabriel  =  0
nulo  =  0
branco  =  0
total  =  0

while  voto  !=  0 :
    voto  =  int ( input ( "Digite o seu voto:" ))
    if  voto  ==  1 :
        Joao  +=  1
        total  +=  1
    elif  voto  ==  2 :
        Maria  +=  1
        total  +=  1
    elif  voto  ==  3 :
        Leonardo  +=  1
        total  +=  1
    elif  voto  ==  4 :
        Gabriel  +=  1
        total  +=  1
    elif  voto  ==  5 :
        nulo  +=  1
        total  +=  1
    elif  voto  ==  6 :
        branco  +=  1
        total  +=  1

print ( " \n O total de votos para cada candidato: \n " ,
      f'Joao - { Joao } \n ' ,
      f'Maria - { Maria } \n ' ,
      f'Leonardo - { Leonardo } \n ' ,
      f'Gabriel - { Gabriel } \n ' )

print ( "O total de votos nulos: \n " ,
      f'Votos nulos: { nulo } \n ' )

print ( "O total de votos em branco: \n " ,
      f'Votos branco: { branco } \n ' )

print ( "A porcentagem de votos nulos sobre o total de votos: \n " ,
      "Porcentagem: ", (( nulo / total ) * 100 )  , "%" )

print ( "A porcentagem de votos brancos sobre o total de votos: \n " ,
      "Porcentagem: ",   (( branco / total ) * 100 )  ,"%" )