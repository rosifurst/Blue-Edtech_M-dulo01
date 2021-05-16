# 1. Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

tabuada = int(input("Qual tabuada deseja ver? "))
# 1

if tabuada == 1:
    um = 1
    cont = 1
    for i in range(1,11,1):
        print(um , " x ",cont, " = ", i)
        cont += 1

# 2
elif tabuada == 2:
    dois = 2
    cont = 1
    for i in range(2, 21, 2):
        print(dois, " x ", cont, " = ", i)
        cont += 1

#3
elif tabuada == 3:
    tres = 3
    cont = 1
    for i in range(3, 31, 3):
        print(tres, " x ", cont, " = ", i)
        cont += 1

# 4
elif tabuada == 4:
    quatro = 4
    cont = 1
    for i in range(4, 41, 4):
        print(quatro, " x ", cont, " = ", i)
        cont += 1

#5
elif tabuada == 5:
    cinco = 5
    cont = 1
    for i in range(5, 51, 5):
        print(cinco, " x ", cont, " = ", i)
        cont += 1

#6
elif tabuada == 6:
    seis = 6
    cont = 1
    for i in range(6, 61, 6):
        print(seis, " x ", cont, " = ", i)
        cont += 1

#7
elif tabuada == 7:
    sete = 7
    cont = 1
    for i  in range(7, 71, 7):
        print(sete, " x ", cont, " = ", i)
        cont += 1

#8
elif tabuada == 8:
    oito = 8
    cont = 1
    for i in range(8, 81, 8):
        print(oito, " x ", cont, " = ", i   )
        cont += 1

elif tabuada == 9:
    nove = 9
    cont = 1 
    for i in range(9, 91, 9):
        print(nove, " x ", cont, " = ", i)
        cont += 1

else:
    print("Apenas tabuadas de 1 à 9!")

