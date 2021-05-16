# Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista. Ao final, seu script deverá fornecer a média geral do aluno.

materias  =  int ( input ( "Informe o número de matérias" ))

notas  = []

for  cont  in  range ( materias ):
    nota  =  float ( input ( f'Qual nota você tirou na { cont + 1 } materia?' ))
    notas.append( nota )


print ( "Média: ", sum ( notas ) / materias  )