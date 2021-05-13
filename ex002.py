# Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def soma_num(a, b, limite):
  if (a+b) > limite:
    return True
  else:
    return False


num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
limite = 50

print(soma_num(num1, num2, limite))