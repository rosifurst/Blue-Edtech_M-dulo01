# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


def soma(n1, n2):
    soma = n1 + n2
    print("Soma: ", soma)
    if soma % 2 == 0:
        print(soma, " é um número par!")
    else:
        print(soma, "é um número ímpar!")


def multiplicação(n1, n2):
    mult = n1 * n2

    if mult > 40:
        div = n1 // n2
        numero = mult // div
        print("A multiplicação foi maior que 40: \n", numero)

    else:
        print("A multiplicação não foi maior que 40: \n", mult)


def divisao(n1, n2):
    print("Divisão: %.2f\n" % (n1 / n2))


def maior(n1, n2):
    if n1 > n2:
        print(n1, "É o maior número!")
    elif n2 > n1:
        print(n2, "É o maior número!")


def par_impar(n1, n2):

    if n1 % 2 == 0:
        print(n1, "É par!")
    else:
        print(n1, "é ímpar!")

    if n2 % 2 == 0:
        print(n2, "É par!")
    else:
        print(n2, "é ímpar!")


n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))

while True:

    op = int(input("\nMENU\n"
                   "1 - Soma \n"
                   "2 - Multiplicação \n"
                   "3 - Divisão \n"
                   "4 - Maior número \n"
                   "5 - Par ou impar \n"
                   "6 - Sair\n"
                   "OPÇÃO: \n"))

    if op == 1:
        soma(n1, n2)

    elif op == 2:
        multiplicação(n1, n2)

    elif op == 3:
        divisao(n1, n2)

    elif op == 4:
        maior(n1, n2)


    elif op == 5:
        par_impar(n1, n2)

    elif op == 6:
        break

    else:
        print("Opção inválida!")
