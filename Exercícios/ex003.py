#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint



usuario = input("informe seu nome de usuário para cadastro:")
senha = input("Informe uma senha para cadastro:")

while usuario == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")

print("Cadastro aprovado")

login = input("informe o seu nome de usuário: ")

while login != usuario:
    print("Login incorreto, tente novamente!")
    login = input("Informe o seu nome de usuário: ")

key = input("Informe a sua senha: ")


while key != senha:
    print("Senha incorreta, tente novamente: ")
    key = input("Informe a sua senha: ")

print("Bem vindo ao jogo da adivinhação! será que você consegue adivinhar o número que eu estou pensando ?!")
computador = randint(0, 20)


print("Vou pensar num número de 0 a 20, tente adivinhar !")

acertou = False
acertou = 0

while not acertou:
    jogador = int(input("E aí, qual o seu palpite ? ( de 0 a 10): "))

    if jogador == computador:
        acertou = True
        print(f"Você acertou !!! eu pensei exatamente no número {computador}")
    else:
        if jogador < computador:
            print(
                f"Hmm... não foi dessa vez, eu pensei num número maior que {jogador}")
        elif jogador > computador:
            print(
                f"Hmm... não foi dessa vez, eu pensei num número menor que {jogador}")