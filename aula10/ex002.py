#Exercício 2 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.

opc  =  True

while  opc  ==  True :
    senha  =  input ( "Digite a senha:" )
    if  senha  ==  '1234' :
        opc  =  False
    while  senha  !=  '1234' :
        print( "Tente novamente!!" )
        senha  =  input ( "Digite a senha:" )


print( "Senha correta!" )