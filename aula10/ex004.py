# Exercício 4 – Codifique um jogo da FORCA. A pessoa digita uma palavra e tem que acertar a palavra digitada.

opc  =  1

while opc  ==  1 :
    palavra  =  input( "Digite a palavra correta:" ).upper()

    while  palavra  !=  "PROGRAMADOR" :
        print()
        print ( "Palavra incorreta!" )
        print()
        palavra  =  input( "Digite a palavra correta:" )

    if  palavra  ==  "PROGRAMADOR" :
        print()
        opc  =  0
        print ( "Palavra correta!" )