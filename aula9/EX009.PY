# 9. Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
	#Dados:
	#Cada palpite possui 6 dezenas
	#As dezenas variam de 1 até 60
	#Não pode repetir dezena

from random import randint
print("      JOGO DA MEGA SENA     ")


lista = list()
jogos = list()
quant = int(input("Informe a quantidade de sorteios: "))

total = 1

while total <= quant:
    cont = 0
    while cont <= 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f'Sorteando {quant} Jogos')

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')