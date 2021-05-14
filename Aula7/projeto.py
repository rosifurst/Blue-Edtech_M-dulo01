# PROJETO: Gastos com viagem -  Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
# Hospedagem
# 1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

def custo_hotel(noites):

    noites = noites * 140.00
    return noites



# Passagem
# 2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
# - São Paulo custa R$ 312,00;
# - Porto Alegre custa R$ 447,00;
#- Recife custa R$ 831,00;
#- Manaus custa R$ 986,00.
# Aluguel de Carro


def custo_aviao(nome_cidade):
    custo = 0.0
    if nome_cidade == "SP":
        custo = 312.00
    elif nome_cidade == "PA":
        custo = 447.00
    elif nome_cidade == "RC": 
        custo = 831.00
    elif nome_cidade == "MN":
        custo = 986.00
    return custo


#3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
#- Calcule o custo do aluguel do carro sendo que:
#- A cada dia o carro custa R$ 40,00;
#- Alugando 7 dias ou +: R$ 50,00 de desconto;
#- Alugando 3 dias ou +: R$ 20,00 de desconto;
# - Você pode receber apenas um desconto;
#- Retorne o custo.
#Cálculo Total

def custo_carro(dias):
    custo = dias*40.00
    if dias >= 7:
        custo = custo - 50.00
    elif dias < 7 and dias >= 3:
        custo = custo - 20.00
    return custo



#4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
#- Reutilize as funções já criadas.
#- Exiba o total da viagem chamando apenas a nova função declarada!
#Gastos Extras
#5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
#Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.

def  custo_total ( cidade , qtdDias , gastos_extras ):
    noites  =  int ( input ( f'Você irá dormir quantas noites em { cidade } ?:' ))
    valorTotal  =  custo_hotel ( qtdDias ) +  custo_aviao ( cidade ) +  custo_carro ( qtdDias )
    valorTotal  =  valorTotal  +  gastos_extras
    return  valorTotal

cidade  =  input ( "Digite a cidade de destino, 'SP' para São Paulo, 'PA' para Porto Alegre, 'RC' para Recife ou 'MN' para Manaus:" )

qtdDias  =  int ( input ( f'Informe a quantidade de dias da sua viagem para { cidade } :' ))
gastos_extras  =  float ( input ( "Informe o valor caso tenha tido algum gasto extra, se não digite 0:" ))

print( f'O custo para viagem informada é { custo_total ( cidade , qtdDias , gastos_extras ) } ')

