from random import randint
print(70 * "\033[1;32m=\033[m")
numero = int(input("\033[1;33mO computador vai pensar em um número entre 0 e 5, tente adivinhar: "))
print(70 * "\033[1;34m=\033[m")
numero_sorteio = randint(0,5)
# print("O número pensado foi {}.".format(numero_sorteio))

if numero == numero_sorteio:
    print("\033[1;32mPARABÉNS, você venceu! :D\033[m")
else:
    print("\033[1;31mVocê errou! :(\033[m")