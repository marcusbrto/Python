import random
jogador = str(input("Você quer pedra, papel ou tesoura? ")).lower()
computador = random.choice(["pedra", "papel", "tesoura"])

if jogador == computador:
    print("Empate")
elif jogador == "papel" and computador == "pedra":
    print("Você venceu!")
elif jogador == "pedra" and computador == "tesoura":
    print("Você venceu!")
elif jogador == "tesoura" and computador == "papel":
    print("Você venceu!")
else:
    print("Computador venceu!")