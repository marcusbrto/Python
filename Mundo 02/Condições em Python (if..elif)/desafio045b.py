from random import randint #é que faz as escolhas aleatorias
from time import sleep #só para ter um timerzinho quando falar jokenpo
itens = ('Pedra', 'Papel', 'Tesoura')#item 0, 1 e 2
computador = randint(0, 2)#ele escolhe aleatoriamente algum item da lista
print("-=" * 11)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual sua jogada? "))

print("\033[35mJO\033[m") #meramente pra ficar legalzinho
sleep(1)
print("\033[34mKEN\033[m")
sleep(1)
print("\033[33mPO!!\033[m")

if jogador > 2 or jogador < 0: #em caso de jogada invalida
    print("\033[41mOPÇÃO INVÁLIDA, SERÁ ESCOLHIDA UMA OPÇÃO ALEATÓRIA\033[m")
    jogador = randint(0, 2)

print("-=" * 11)
print(f"Computador escolheu {itens[computador]}") #escreve o item da lista que ele escolheu, o itens[computador] é importante para ele escrever o que tiver na lista
print(f"Jogador jogou {itens[jogador]}")
print("-=" * 11)

if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print("\033[37mEMPATE\033[m")
    elif jogador == 1:
        print("\033[32mJOGADOR VENCEU\033[m")
    elif jogador == 2:
        print("\033[31mCOMPUTADOR VENCEU\033[m")
    else:
        print("\033[42mJOGADA INVÁLIDA\033[m")
elif computador == 1: #Computador jogou papel
    if jogador == 1:
        print("\033[37mEMPATE\033[m")
    elif jogador == 2:
        print("\033[32mJOGADOR VENCEU\033[m")
    elif jogador == 0:
        print("\033[31mCOMPUTADOR VENCEU\033[m")
    else:
        print("\033[42mJOGADA INVÁLIDA\033[m")
elif computador == 2: #Computador jogou tesoura
    if jogador == 2:
        print("\033[37mEMPATE\033[m")
    elif jogador == 0:
        print("\033[32mJOGADOR VENCEU\033[m")
    elif jogador == 1:
        print("\033[31mCOMPUTADOR VENCEU\033[m")
    else:
        print("\033[42mJOGADA INVÁLIDA\033[m")