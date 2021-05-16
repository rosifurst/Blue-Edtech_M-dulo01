# 8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# ○ “Telefonou para a vítima?”
# ○ “Esteve no local do crime?”
# ○ “Mora perto da vítima?”
# ○ “Devia para a vítima?”
# ○ “Já trabalhou com a vítima?”
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino”. Caso contrário, ele será classificado como “Inocente”.

resp1 = input("Telefonou para a vítima? (sim/não)").upper()
resp2 = input("Esteve no local do crime? (sim/não)").upper()
resp3 = input("Mora perto da vítima? (sim/não)").upper()
resp4 = input("Devia para a vítima? (sim/não)").upper()
resp5 = input("Já trabalhou com a vítima? (sim/não)").upper()

respostas = [resp1, resp2, resp3, resp4, resp5]
cont = 0

for i in respostas:

    if i == "SIM":
        cont += 1

if cont == 2:
    print("SUSPEITO!")

elif cont >= 3 and cont <= 4:
    print("CÚMPLICE!")

elif cont == 5:
    print("ASSASSINO!")

else:
    print("INOCENTE!")

