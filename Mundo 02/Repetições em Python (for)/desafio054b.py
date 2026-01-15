from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input(f"Digite o ano a {pess} nasceu: "))
    idade = (atual - nasc)
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f"Ao todo tivemos {totalmaior} pessoas maiores de idade\nE tambem tivemos {totalmenor} pessoas menores de idade")