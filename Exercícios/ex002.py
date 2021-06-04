# 02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input("Digite uma frase:").lower()

vogais = 0
for letra in frase:
    if letra in "aeiou":
        vogais += 1

resposta = ''
for letra in frase:
    if letra not in 'aeiou':
        resposta += letra

print()
print(f'O resultado da frase " {resposta} ". ')
print()
print(f'Foram retiradas {vogais} letras. ')

print(frase)
