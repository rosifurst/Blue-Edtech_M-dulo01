#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

# 02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.


def verificaVogais(frase): # função para contar as vogais
    vogais = 0
    for letra in frase:
        if letra in "aeiou":
            vogais += 1
    return vogais


def retornaFrase(frase): # função que retorna as frases sem vogais
    resposta = ''
    for letra in frase:
        if letra not in 'aeiou':
            resposta += letra
    return resposta


frase = input("Digite uma frase:").lower()
print()
print(f'O resultado da frase " {retornaFrase(frase)} ". ')
print()
print(f'Foram retiradas {verificaVogais(frase)} letras. ')

print(frase)
