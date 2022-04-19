
import random

def jogar():

    print("*********************************")
    print("bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = (random.randrange(1,51))
    total_de_tentativas = 0
    pontos = 500
    print("Qual Nível de dificuldade?")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = int(input("Selecione o Nível:"))

    if(nivel == 1):
        total_de_tentativas = 8
    elif(nivel == 2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 4

    for rodada in range(1, total_de_tentativas +1):
        print("tentativa {} de {}".format(rodada,total_de_tentativas))

        chute_str = input("Digite um numero entre 1 e 50: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 50):
            print("voce deve digitar um numero entre 1 e 50!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos! ".format(pontos))
            break
        else:
            if(maior):
                print("Você errou ! Seu chute foi maior que o numero secreto !")
            elif(menor):
                print("Você errou ! Seu chute foi menor que o numero secreto !")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo")

if(__name__=="__main__"):
    jogar()
