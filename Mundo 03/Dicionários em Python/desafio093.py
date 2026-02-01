soma = 0
jogador = dict()
jogador["gols"] = []
jogador["nome"] = str(input("Nome do Jogador: "))
jogador["qnt"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for c in range(jogador["qnt"]):
    gols = int(input((f"Quantos gols na partida {c}? ")))
    jogador["gols"].append(gols)
    soma += gols
print("-=" * 40)
print(jogador)
print("-=" * 40)
print(f"O campo nome tem o valor {jogador['nome']}")
print(f"O campo gols tem o valor {jogador["gols"]}")
print(f"O campo total tem o valor {soma}")
print("-=" * 40)
print(f"O jogador {jogador["nome"]} jogou {jogador['qnt']} partidas.")
for c in range(jogador["qnt"]):
    print(f"Na partida {c}, fez {jogador['gols'][c]} gols.")
print(f"Foi um total de {soma} gols.")