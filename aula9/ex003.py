#c 3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e mostre ao final a quantidade de pessoas de cada estado civil. 
Nome = []
estciv = []

cont1 = 0
cont2 = 0

for i in range(0, 3, 1):

    nome = input("Nome: ")
    estado_civil = input("Estado Civil: ").upper()

    if estado_civil == "SOLTEIRO" or estado_civil == "SOLTEIRA":
        cont1 += 1
    else:
        cont2 += 1
    

    Nome.append(nome)
    estciv.append(estado_civil)



print("Pessoas Solteiras: ", cont1)
print("Pessoas Casadas: ",cont2)
