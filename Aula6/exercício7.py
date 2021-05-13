#7.	Escreva uma função que recebe dois 
# parâmetros 
# e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.

def menor_igual(num1, num2):
    if num1 < num2:
        return "Menor número: %d" % num1
    elif num1 == num2:
        return "São iguais!"
    else:
        return num2
print(menor_igual(5,55))