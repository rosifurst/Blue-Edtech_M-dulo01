
#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = []


for cont in range(7):
    numero = int(input("Digite o %d° numero: " % (cont + 1)))
    numeros += [numero]
print()


lista = []
impares = []

for cont in numeros:
    if cont % 2 == 0:
        lista += [cont]
    else:
        impares += [cont]
print()

lista.sort()
impares.sort()

lista.extend(impares)

print(lista)