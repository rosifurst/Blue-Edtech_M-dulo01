print("FUNÇÕES")

# Definindo uma função

def blue():
    print("Eu sou um Blumer")

# chamar a função
blue()

print("Exemplo de função com parâmetros")


#definindo a função 

def subtracao(a, b):
    print("A subtração entre %d e %d é : %d"%(a, b, (a - b)) )



#definindo a função 

def soma(c, d):
    print("A soma entre %d e %d é: %d" %(c, d, (c + d)) )


#definindo a função 

def multiplicacao(e, f):
    print("A multiplicação entre %d e %d é %d: " % (e, f, (e*f)))

def divisao(g, h):
    print("A divisão entre %d e %d é : %.2f " % (g, h, (g/h)))

#chamando a função



subtracao(10,5)
soma(5, 10)
multiplicacao(5, 10)
divisao(5, 10)

