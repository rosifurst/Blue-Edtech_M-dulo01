# . Faça um programa que mostre os valores numéricos inteiros ímpares situados na faixa de 0 a 20. 

for i in range(0, 21, 1):
    if i % 2 != 0:
      print(i)