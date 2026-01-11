import random
numero = int(input("O computador vai pensar em um número entre 0 e 5, tente adivinhar: "))
numero_sorteio = random.randint(0,5)
if numero == numero_sorteio:
    print("Você acertou! :D")
else:
    print("Você errou! :(")