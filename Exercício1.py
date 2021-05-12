# Exercício 1  - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparecem as vogais a,e,i,o,u

def vogais(frase):

   count = 0

   for i in frase:
       if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
           count += 1
        
       if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            count += 1

       print(i)

   print("As vogais aparecem %d vez(es)" % count)



vogais(input("Frase: "))