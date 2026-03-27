from random import randint
computador = randint(0, 10)
palpites = 0
print("Sou seu computador... Acabei de pensar em um numero entre 0 e 10")
print("Será que você consegue adivinhar?")
acertou = False
while not acertou: #enquanto acertou for false ele vai repetir até receber True
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1 #só para contar a quantidade de tentativas
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador: #se jogador jogou um numero menor que do computador ele printa isso
            print("Mais... Tente mais uma vez")
        else:
            print("Menos... Tente mais uma vez")
print(f"\033[1;32mParabéns! Você acertou em {palpites} tentativas.\033[m")
