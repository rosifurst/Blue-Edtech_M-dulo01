#5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
# peso / altura **2
def IMC(altura, peso):
    imc = peso / (altura**2)
    return "Cálculo IMC %.2f" % imc
print(IMC(1.68, 75))