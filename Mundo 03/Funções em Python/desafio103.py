def ficha(jogador, gols):
    print(f"O jogador {jogador} fez {gols} gol(s)")

nome = input("Digite o nome do jogador: ").strip()
gols = input("Digite o número de gols: ")

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == "":
    ficha("DESCONHECIDO", gols)
else:
    ficha(nome, gols)
