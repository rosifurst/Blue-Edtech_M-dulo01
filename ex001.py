# Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênticos.


def menor(num1, num2):
    if num1 < num2:
        print("Menor: ", num1)
    elif num1 > num2:
        print("Menor: ", num2)
    else:
        print("%d e %d são idênticos!" % (num1, num2))





valor1 = int(input("Número 1: "))
valor2 = int(input("Número 2: "))

print(menor(valor1, valor2))