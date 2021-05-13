# Exercício 6 Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média. Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.


def media(nota1, nota2, nota3):
    # média das 3 notas
    media = float((nota1 + nota2 + nota3)/ 3)
    
    print("Média de todas as notas: ", media)
    
    # média das notas mais altas

    if nota1 > nota2 and nota2 > nota3:
        print(f'Média das notas mais altas: {(nota1 + nota2)/ 2}')

    elif nota3 > nota2 and nota1 > nota2:
        print(f'Média das notas mais altas: {(nota1 + nota3)/ 2}')
    
    if nota2 > nota1 and nota3 > nota1:
        print(f'Média das notas mais altas: {(nota2 + nota3)/2}')
    
    # maior nota

    maior = nota1

    if nota2 > maior:
        maior = nota2
    if nota3 > maior:
        maior = nota3

    print(f'Nota maior: {maior}')

    # Menor nota

    menor = nota1
    if nota2 < menor:
        menor = nota2
    if nota3 < menor:
        menor = nota3  
    


    print(f'Nota menor: {menor}')


nota1= float(input("1° nota: "))
nota2 = float(input("2° nota: "))
nota3 = float(input("3° nota: "))

print()

media(nota1, nota2, nota3)