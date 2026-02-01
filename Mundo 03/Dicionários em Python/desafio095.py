jogador = dict()
partidas = list()
time = list()
while True:
    jogador["nome"] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range (0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c}? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    while True:
        confirmar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        if confirmar in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if confirmar == "N":
        break
print("-="*50)
print(f"{'cod':<4}{'nome':<10}{'gols':>13}{'total':>11}")
print("--"*50)
for i,j in enumerate(time):
    print(f"{i:<4}{j['nome']:<10}{str(j['gols']):>10}{j['total']:>8}")

while True:
    print("-"*50)
    opc = int(input("Mostrar dados de qual jogador? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(time)-1:
        print(f"Levantamento do jogador {time[opc]['nome']}")
        for idx, g in enumerate(time[opc]["gols"]):
            print(f"   Jogo {idx + 1}: {g} gols")
    if opc > len(time)-1:
        print(f"ERRO! Não existe jogador com código {opc}!")


