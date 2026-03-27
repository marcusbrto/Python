def ficha(jog="<DESCONHECIDO>",gol=0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")


nome = str(input("Digite o nome do jogador: "))
gols = str(input("Digite a quantidade de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gol=gols)
else:
    ficha(nome,gols)