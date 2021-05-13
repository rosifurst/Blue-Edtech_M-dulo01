#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
#  se seu argumento for positivo, ‘N’, 
# se seu argumento for negativo e ‘0’ se for 0.

def valor(x):
    if x > 0:
        return "P"
    elif x < 0:
        return "N"
    elif x == 0:
        return "0"
print(valor(0))