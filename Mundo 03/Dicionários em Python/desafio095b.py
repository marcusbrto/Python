time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["nome"] = str(input("Qual o nome do jogador: "))
    partidas.clear()
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range (0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c+1}? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == "N":
        break
print("-="*30)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15} ", end="")
print()
print("-="*40)
for k,j in enumerate(time):
    print(f"{k:>3}", end="")
    for d in j.values():
        print(f" {str(d):<15}", end="")
    print()
print("-="*30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"   No jogo {i+1} fez {g} gols")
    print("-="*30)
print("<< VOLTE SEMPRE >>")