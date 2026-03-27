from random import randint
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    jogada = str(input("Qual sua jogada? Par ou Impar: ")).lower().strip()
    sorteio = randint(1, 10)
    num = sorteio
    num += valor
    if num % 2 == 0:
        result = "PAR"
    else:
        result = "IMPAR"
    print(f"Você jogou {valor} e o computador jogou {sorteio}. Total de {num} DEU {result}")
    if jogada == "par" and result == "PAR":
        print("Você VENCEU!")
        cont += 1
    elif jogada == "impar" and result == "IMPAR":
        print("Você VENCEU!")
        cont += 1
    else:
        print("Você PERDEU!")
        break
print(F"GAME OVER! Você venceu {cont} vezes.")
