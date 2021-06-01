# Integrantes do grupo:
# Sergio
# Rosicleia Furst
# Lucas Castorino

# A ideia inicial era fazer pequenas alterações no programa incluindo alguns eventos aleatórios.
# Ao decorrer do desenvolvimento mudamos a ideia para criar um labirinto onde o personagem tem que vencer um minotauro para escapar.
# Fomos discutindo e juntando ideias enquanto faziamos o código para o jogo.
# Aplicamos praticamente tudo o que foi visto no curso para o desenvolvimento.

# Importando funções
from random import randint
from time import sleep
from time import time


# Definindo as classes:


class Relogio2:
    def __init__(self):
        self.horas = 4

    def __str__(self):
        return f"Você tem: {self.horas}horas"

    def perdeTempo(self, horas):
        self.horas -= horas


class Relógio:
    def __init__(self, i, f):
        self.minutos = (f - i) // 60
        self.segundos = (f - i) - self.minutos * 60

    def __str__(self):
        return f"Tempo de jogo: {self.minutos:.0f} minutos e {self.segundos:.0f} segundos"


class Personagem:
    def __init__(self):
        self.contas = False
        self.compras = False
        self.nome = ""
        self.força = 10
        self.carisma = 10
        self.pontaria = 10
        self.agilidade = 10
        self.dinheiro = 1000




    def __str__(self):
        return " Você é um herói, mas antes de salvar o mundo você " \
               "" + ("já pagou" if self.contas else "precisa pagar") + \
               " suas contas, " + ("você fez as" if self.compras else "e precisa fazer") + \
               " compras!  Você precisa ser rápido! "

    def apostar(self):
        if self.dinheiro >= 10:
            self.dinheiro -= 10
            r = randint(1, 100)
            if r == 100:
                print("você ganhou 1 milhão!!!")
                sleep(1)
                self.dinheiro += 1000000000
            else:
                print("dinheiro-10\nvocê perdeu")
                sleep(1)
        else:
            print("Você não tem dinheiro")


class Heroi(Personagem):
    def __init__(self):
        super().__init__()
        self.__nivel = 1
        self.vida = True

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, n):
        raise ValueError(
            "Impossível alternar diretamente. Use a função Evoluir().")

    def Evoluir(self, n):
        self.__nivel += n

    # metodo que passa todos os atributos de um objeto pra uma nova classe

    def Subir_de_classe(self, heroi):
        self.nome = heroi.nome
        self.força = heroi.força
        self.agilidade = heroi.agilidade
        self.carisma = heroi.carisma
        self.pontaria = heroi.pontaria

    def __str__(self) -> str:
        return f"\n {self.nome} nível {self.nivel}\nForça: {self.força},  Agilidade: {self.agilidade}\nCarisma: {self.carisma},  Pontaria: {self.pontaria}"

    # frase de impacto quando heroi vence

    def comemora_vit(self, atributo, qtd, nivel):
        print(f"Vitória!\n\n{atributo}+{qtd} e nível+{nivel}")

    # contrutor: molde das açoes recebendo os paramentros que serão usados

    def Açoes(self, inimigo, opção, lista, conv, fugiu):
        if inimigo == "Coruja":
            if opção == "1":
                print(
                    "Você atacou a pobre coruja indefesa, coitada\nVocê passou pelo inimigo!\n")
                self.força += 10
                self.Evoluir(1)
                lista.append("Coruja")
                self.comemora_vit("força", 10, 1)
            elif opção == "2":
                print("A coruja contou que o minotauro possui força 50!")
                sleep(1)
                print("Você passou pelo inimigo!\n")
                conv.append("Coruja")
                self.Evoluir(1)
                self.carisma += 10
                self.comemora_vit("carisma", 10, 1)
            elif opção == "3":
                print("Você passou pelo inimigo!\n")
                self.Evoluir(1)
                self.agilidade += 10
                self.comemora_vit("agilidade", 10, 1)
            elif opção == "4":
                print("Você atirou uma pedra:")
                sleep(1)
                print("Acertou em cheio!\n")
                sleep(1)
                print("Você passou pelo inimigo")
                self.Evoluir(1)
                lista.append("Coruja")
                self.pontaria += 10
                self.comemora_vit("pontaria", 10, 1)
            else:
                fugiu[0] += 1
                print("você fugiu!")
            sleep(1)
        elif inimigo == "Morcego":
            if opção == "1":
                print(
                    "Você atacou a morcego, ele te mordeu\n\n\tVocê morreu!\n")
                sleep(3)
                self.vida = False
            elif opção == "2":
                print("O morcego contou que o minotauro tem magia 50!")
                sleep(1)
                print("Você passou pelo inimigo!\n")
                self.Evoluir(1)
                conv.append("Morcego")
                self.carisma += 10
                self.comemora_vit("carisma", 10, 1)
            elif opção == "3":
                if self.agilidade >= 20:
                    print("Você conseguiu desviar do inimgo!\n")
                    self.Evoluir(1)
                    self.agilidade += 10
                    self.comemora_vit("agilidade", 10, 1)
                else:
                    print("\n\tVocê Morreu!\n")
                    self.vida = False
                    sleep(3)
            elif opção == "4":
                print("Você atirou uma pedra:")
                sleep(1)
                if self.pontaria >= 20:
                    print("Acertou em cheio!\n")
                    sleep(1)
                    self.Evoluir(1)
                    lista.append("Morcego")
                    self.pontaria += 10
                    self.comemora_vit("pontaria", 10, 1)
                else:
                    print(
                        "Você errou! mas assustou o morcego, você pode passar\n")
            else:
                fugiu[0] += 1
                print("você fugiu!")
            sleep(1)
        elif inimigo == "Iguana":
            if opção == "1":
                if self.força > 20:
                    print(
                        "Você deu uma bicuda na Iguana\nVocê passou pelo inimigo!\n")
                    self.força += 15
                    self.Evoluir(1)
                    lista.append("Iguana")
                    self.comemora_vit("força", 15, 1)
                else:
                    print("\n\tVocê Morreu!\n")
                    self.vida = False
            elif opção == "2":
                print(
                    "A Iguana contou que o Minotauro só fala com quem tem carisma 70!")
                sleep(1)
                print("Você passou pelo inimigo!\n")
                conv.append("Iguana")
                self.Evoluir(1)
                self.carisma += 10
                self.comemora_vit("carisma", 10, 1)
            elif opção == "3":
                print("\n\tVocê Morreu!\n")
                self.vida = False
            elif opção == "4":
                print("Você atirou uma pedra:")
                sleep(1)
                if self.pontaria > 20:
                    print("Acertou em cheio!\n")
                    sleep(1)
                    print("Você passou pelo inimigo")
                    self.Evoluir(1)
                    self.append("Iguana")
                    self.pontaria += 10
                    self.comemora_vit("pontaria", 10, 1)
                else:
                    print("\n\tVocê Morreu!\n")
                    self.vida = False
            else:
                print("Você fugiu!")
                fugiu[0] += 1
            sleep(1)
        elif inimigo == "Minotauro":
            if opção == "0":
                fugiu[0] += 1
                print("Você Fugiu!")
            else:
                print("\n\tVocê Morreu!\n")
                sleep(3)
                self.vida = False
            sleep(1)

    # esse metodo é o contrutor quando uma classe enfrenta o minotauro, e sera herdada por todas as classes

    def Enf_minotauro(self, opção, lista, conv, fugiu):
        self.vida = False
        if opção == "1":
            if self.força > 50:
                print(
                    "\n\tVocê derrotou o Minotauro!!\n\tParabéns!\n\tVocê conseguiu escapar do labirinto.\n")
                sleep(3)
                lista.append("Minotauro")
            else:
                print("\n\tVocê Morreu!\n")
                sleep(3)
        elif opção == "2":
            if self.carisma >= 70:
                print(
                    "\n\tVocê se tornou amigo do Minotauro!\n\tParabéns!\n\tVocê escapou do labirinto.")
                sleep(3)
                conv.append("Minotauro")
            else:
                print("O Minotauro não estava para conversa")
                sleep(1)
                print("\n\tVocê Morreu!\n")
                sleep(3)
        elif opção == "3":
            print("\n\tVocê Morreu!\n")
            sleep(3)
        elif opção == "4":
            print("\n\tVocê Morreu!\n")
            sleep(3)
        else:
            self.vida = True
            fugiu[0] += 1
            print("Você fugiu!")


# Subclasses da classe Heroi:


class Mago(Heroi):
    def __init__(self):
        super().__init__()
        self.magia = 10

    def __str__(self) -> str:
        return f"\n{self.nome} Mago nível {self.nivel}\nForça: {self.força},  Agilidade: {self.agilidade}\nCarisma: {self.carisma},  Pontaria: {self.pontaria}\nMagia: {self.magia}"

    def comemora_vit(self, atributo, qtd, nivel):
        print("\nNão vai passar.\n")
        sleep(1)
        print(f"{atributo}+{qtd} e nível+{nivel}")

    # açoes proprias do mago relacionadas a opção5, magia, inclementando as açoes da superclasse mas vindo antes

    def Açoes_mago(self, inimigo, lista):
        if inimigo == "Minotauro":
            self.vida = False
            if self.magia > 50:
                print(
                    "\n\tVocê derrotou o Minotauro!!\n\tParabéns!\n\tVocê conseguiu escapar do labirinto.\n")
                sleep(3)
                lista.append("Minotauro")
            else:
                print("\n\tVocê Morreu!\n")
                sleep(3)
        else:
            print(f"Você congelou a(o) {inimigo}!\n")
            sleep(1)
            lista.append(inimigo)
            self.Evoluir(1)
            self.magia += 10
            self.comemora_vit("magia", 10, 1)


class Atirador(Heroi):
    def __init__(self):
        super().__init__()
        self.poder_de_fogo = 30

    def __str__(self) -> str:
        return f"\n{self.nome} Atirador nível {self.nivel}\nForça: {self.força},  Agilidade: {self.agilidade}\nCarisma: {self.carisma},  Pontaria: {self.pontaria}\nPoder de Fogo: {self.poder_de_fogo}"

    def comemora_vit(self, atributo, qtd, nivel):
        print("\nNão basta acertar o alvo, tem que atingir o objetivo.\n")
        sleep(1)
        print(f"{atributo}+{qtd} e nível+{nivel}")

    # açoes do atirador

    def Açoes_atirador(self, inimigo, lista):
        if inimigo == "Minotauro":
            self.vida = False
            if self.poder_de_fogo > 150:
                print(
                    "\n\tVocê derrotou o Minotauro!!\n\tParabéns!\n\tVocê conseguiu escapar do labirinto.\n")
                sleep(3)
                lista.append("Minotauro")
            else:
                print("Bang!")
                sleep(1)
                print("Você Errou!")
                print("\n\tVocê Morreu!\n")
                sleep(3)
        else:
            print("Bang!\n")
            sleep(1)
            print(f"Você estourou os miolos da(o) {inimigo}!\n")
            self.Evoluir(1)
            sleep(1)
            lista.append(inimigo)
            self.poder_de_fogo += 30
            self.comemora_vit("poder de fogo", 30, 1)


class Inimigo:
    def __init__(self):
        self.inimigo = ""

    # classe com atributo vazio e metodo que define aleatoriamente um elemento de uma lista

    def def_inimigo(self):
        inimigos = ["Coruja", "Morcego", "Minotauro", "Coruja", "Iguana"]
        r = randint(0, len(inimigos) - 1)
        for i in range(len(inimigos)):
            if r == i:
                self.inimigo = inimigos[i]

    # metodo que recebe uma lista, separa elementos iguais e imprimi k e v de um dicionario

    def derrotados(self, lista):
        derrotados = [[], [], []]
        for i in lista:
            if i == "Coruja":
                derrotados[0].append(i)
            elif i == "Morcego":
                derrotados[1].append(i)
            elif i == "Iguana":
                derrotados[2].append(i)
        dic = {}
        dic["Coruja(s)"] = len(derrotados[0])
        dic["Morcego(s)"] = len(derrotados[1])
        dic["Iguana(s)"] = len(derrotados[2])
        if "Minotauro" in lista:
            dic["Minotauro"] = 1
        for k, v in dic.items():
            print(f"{v} - {k} ")

    # como a classe retorna quando chamada

    def __str__(self):
        return f"\n\t\t\t- {self.inimigo} -\n"


# classe cenario, tem como atributo uma lista e retorna no str um elemento aleatorio da lista


class Field():
    def __init__(self):
        self.field = ['''
1 em frente
2- virar a direita
        ________________________
    >>> ___________   __________
                   |  |
                   |  |
                   |  |            ''', '''
1- para cima
2- para baixo

                   |  |
         __________|  |
    >>>  __________   |
                   |  |
                   |  |''', '''
1- para esquerda
2- em frente
                   |  |
                   |  |
         __________|  |_____
    >>>  ___________________''']

    def __str__(self):
        r = randint(0, len(self.field) - 1)
        for i in range(len(self.field)):
            if r == i:
                return f"{self.field[i]}"


if __name__ == "__main__":
    relogio2 = Relogio2()
    personagem = Personagem()

    print("\t●▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬●\n"
          "\t\tAMAZING  HERO\n"
          "\t●▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬●\n")

    personagem.nome = input("\n\tDigite o nome do personagem: ")
    mercado = {"Carne": ["+10 força", " R$ 50,00 ", "1"],
               "Sabonete": ["+10 carisma", " R$ 30,00", "2"],
               "Óculos": ["+10 pontaria", "R$ 80,00", "3"],
               "Café": ["+10 agilidade", "R$ 40,00", "4"]}

while True:

    print(f"\n{personagem}\nPara onde você quer ir?: \t\t{relogio2}")
    opcao = int(input("1 - Mercado.\n"
                      "2 - Lotérica.\n"
                      "3 - Praia.\n"
                      "4 - Salvar o Mundo.\n"
                      "5 - Sair.\n"
                      "Selecione a opção:"))

    if opcao == 1:
        relogio2.perdeTempo(1)
        print("\n\tMercado\t\tvocê tem R$ ", personagem.dinheiro)
        print()
        for k in mercado:
            print(k, end=" / ")
        print()
        print()
        op = int(input("1 --> Comprar.\n"
                       "0 --> Voltar.\n"
                       "Selecione opção:"))

        if op == 1:
            personagem.compras = True
            for k, v in mercado.items():
                print(f"{v[2]} - {k} - {v[1]} - {v[0]}")
            op1 = int(input("Selecione opção: "))
            if op1 == 1:
                if personagem.dinheiro < 50:
                    print("Você esta devendo")
                print("força+10\ndinheiro-50")
                personagem.dinheiro -= 50
                personagem.força += 10
            elif op1 == 2:
                if personagem.dinheiro < 30:
                    print("Você esta devendo")
                print("carisma+10\ndinheiro-30")
                personagem.dinheiro -= 30
                personagem.carisma += 10
            elif op1 == 3:
                if personagem.dinheiro < 80:
                    print("Você esta devendo")
                print("pontaria+10\ndinheiro-80")
                personagem.dinheiro -= 80
                personagem.pontaria += 10
            elif op1 == 4:
                if personagem.dinheiro < 40:
                    print("Você esta devendo")
                print("agilidade+10\ndinheiro-40")
                personagem.dinheiro -= 40
                personagem.agilidade += 10

            else:
                print("Não comprou nada")
                personagem.compras = False
    elif opcao == 2:
        relogio2.perdeTempo(1)
        print("\n\tLoterica\t\tvocê tem R$", personagem.dinheiro)
        print()
        print("1 Pagar as contas")
        print("2 Fazer uma aposta")
        print("0 Voltar")
        opção = input("Selecione opção: ")
        if opção == "1":
            if personagem.contas is True:
                print("Você já pagou suas contas")
            else:
                print("Você pagou suas contas\ndinheiro-500")
                sleep(1)
                if personagem.dinheiro < 500:
                    print("Você esta devendo")
                personagem.dinheiro -= 500
                personagem.contas = True
                opção = input("Você também quer fazer uma aposta?S/N ").upper()
                if opção[0] == "S":
                    personagem.apostar()
        elif opção == "2":
            personagem.apostar()

    elif opcao == 3:
        relogio2.perdeTempo(2)
        print("\nVocê foi a praia! estava um dia lindo")
        sleep(1)
    elif opcao == 4:
        if personagem.contas is True and personagem.compras is True:
            if relogio2.horas < 0:
                print("Você se atrasou: força-10 e agilidade-10")
                personagem.força -= 10
                personagem.agilidade -= 10
            inimigo = Inimigo()
            field = Field()
            # while principal para reinicio do jogo
            # while ate o nivel que ele muda de classe, enquanto estiver vivo
            while True:
                # quando voce da enter ele inicia o jgo
                heroi = Heroi()
                heroi.Subir_de_classe(personagem)
                input("\n\tAperte o Enter para começar: ")
                i = time()
                print(
                    "\nVocê precisa atravessar o labirinto para salvar o mundo, para atravessar você precisa derrotar o Minotauro\n"
                    "para derrotar o Minotauro voce precisa evoluir de classe, usar o ataque certo e ter o atributo necessário\n")
                lista = []  # lista de inimigos que vc vai derrotar
                conv = []  # lista de inimigos que vc vai conversar
                fugiu = [0]
                while heroi.vida is True and heroi.nivel < 3:
                    print(f"\t\t{heroi}")
                    print()
                    print(field)
                    print()
                    input("Escolha seu caminho:  ")  # input ilustrativo
                    print()
                    inimigo.def_inimigo()  # defini aleatorio inimigo para chamar a seguir
                    print(
                        f"\t\tVoce encontrou um inimigo:\n {inimigo} \n\t\t  O que você vai fazer? ")
                    print()
                    print("1 - Atacar -")
                    print("2 - Conversar -")
                    print("3 - Desviar -")
                    print("4 - Atirar uma pedra -")
                    print("0 - Fugir - \n")
                    opção = input("Selecione a Ação: ")
                    heroi.Açoes(inimigo.inimigo, opção, lista, conv, fugiu)
                if heroi.vida is True:
                    print("\n\tVocê evoluiu de classe!")
                    print("\n\n\t\t-Mago-\t\t  ou\t\t-Atirador-\n\n")
                    selecione = input("Selecione classe que deseja: ").lower()
                    while selecione != "mago" and selecione != "atirador":
                        selecione = input(
                            "Selecione classe que deseja: ").lower()
                    if selecione == "mago":
                        print(
                            f"\n\n\t{heroi.nome} se tornou um(a) Mago(a)!\n\n")
                        sleep(2)
                        mago = Mago()
                        # transferir atributos pro novo objeto
                        mago.Subir_de_classe(heroi)
                        while mago.vida is True:
                            print(f"\t{mago}")
                            print()
                            print(field)
                            print()
                            input("Escolha seu caminho:  ")
                            print()
                            inimigo.def_inimigo()
                            print(
                                f"\t\tVoce encontrou um inimigo:\n {inimigo} \n\t\t  O que você vai fazer? ")
                            print()
                            print("1 - Atacar -")
                            print("2 - Conversar -")
                            print("3 - Desviar -")
                            print("4 - Atirar uma pedra -")
                            print("5 - Magia - ")
                            print("0 - Fugir - \n")
                            opção = input("Escolha sua opção: ")
                            # as açoes especializadas se aplicam ao menu 5, se não, vai pra açoes padrao
                            if opção == "5":
                                mago.Açoes_mago(inimigo.inimigo, lista)
                            elif inimigo.inimigo == "Minotauro":
                                mago.Enf_minotauro(opção, lista, conv, fugiu)
                            else:
                                mago.Açoes(inimigo.inimigo, opção,
                                           lista, conv, fugiu)
                    # classe atirador
                    elif selecione == "atirador":
                        print(
                            f"\n\n\t{heroi.nome} se tornou um(a) Atirador(a)!\n\n")
                        sleep(2)
                        at = Atirador()
                        at.Subir_de_classe(heroi)
                        while at.vida is True:
                            print(f"\t{at}")
                            print()
                            print(field)
                            print()
                            input("Escolha seu caminho:  ")
                            print()
                            inimigo.def_inimigo()
                            print(
                                f"\t\tVoce encontrou um inimigo:\n {inimigo} \n\t\t  O que você vai fazer? ")
                            print()
                            print("1 - Atacar -")
                            print("2 - Conversar -")
                            print("3 - Desviar -")
                            print("4 - Atirar uma pedra -")
                            print("5 - Arma de fogo - ")
                            print("0 - Fugir - \n")
                            opção = input("Escolha sua opção: ")
                            if opção == "5":
                                at.Açoes_atirador(inimigo.inimigo, lista)
                            elif inimigo.inimigo == "Minotauro":
                                at.Enf_minotauro(opção, lista, conv, fugiu)
                            else:
                                at.Açoes(inimigo.inimigo, opção,
                                         lista, conv, fugiu)
                f = time()
                print(Relógio(i, f))
                print()
                # lista de inimigos enfrentados
                print("Você derrotou:")
                inimigo.derrotados(lista)
                print("Você conversou:")
                inimigo.derrotados(conv)
                print("Você fugiu:", fugiu[0], "vez(es)")
                print()
                print("1 - Reiniciar o labirinto")
                print("2 - Voltar para casa")
                recomeçar = input("Selecione a opção: ")
                while "1" != recomeçar != "2":
                    recomeçar = input("Selecione a opção: ")
                if recomeçar == "2":
                    personagem.dinheiro += 1000
                    personagem.compras = False
                    personagem.contas = False
                    relogio2 = Relogio2()
                    break
    elif opcao == 5:
        break
    else:
        print("Opção inválida!")
