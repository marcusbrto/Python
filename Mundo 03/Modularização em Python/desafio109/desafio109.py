import moeda

p = float(input("Digite o preço: R$"))

while True:
    form = str(input("Quer que os valores sejam formatados? [S/N] ")).strip().upper()[0]

    if form in "SN":
        break
    else:
        print("Resposta inválida. Digite S ou N.")

if form == "S":
    formatado = True
else:
    formatado = False

print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, formatado)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formatado)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10, formatado)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13, formatado)}")
