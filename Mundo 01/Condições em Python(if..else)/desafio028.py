from random import randint
numero = int(input("O computador vai pensar em um número entre 0 e 5, tente adivinhar: "))
numero_sorteio = randint(0,5)
# print("O número pensado foi {}.".format(numero_sorteio))

if numero == numero_sorteio:
    print("PARABÉNS, você venceu! :D")
else:
    print("Você errou! :(")