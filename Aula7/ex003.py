# Exercício Treino 3 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma string.

def converte_maiusculo(palavra):
    return palavra.upper()
    

palavra = input("Digite uma palavra: ")
print(converte_maiusculo(palavra))