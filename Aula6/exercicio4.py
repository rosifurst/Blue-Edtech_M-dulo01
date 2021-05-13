#4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calcularAdicional(salario_hora, horas_trabalhadas):

  tempo = 40
  overtime = horas_trabalhadas- tempo
  horas_trabalhadas -= overtime

  bonus = 1.550
  adicional = (salario_hora * bonus)*overtime
  bonusWage = (salario_hora * horas_trabalhadas) + adicional


  print(f"Com um salário de R${salario_hora:.2f} e {overtime} horas extras")
  print(f"Seu adicional é de R${adicional:.2f} e seu salário final de R${bonusWage:.2f}")

salario_hora = int(input('Entre com seu salário/hora: '))
horas_trabalhadas = int(input('Entre com suas horas totais trabalhadas: '))

calcularAdicional(salario_hora, horas_trabalhadas)
