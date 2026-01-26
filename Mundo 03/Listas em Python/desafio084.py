galera = []
dados = []
pesomaior = []
pesomenor = []
totpessoas = 0
while True:
    galera.append(str(input('Nome: ')))
    galera.append(float(input('Peso: ')))
    if totpessoas == 0:
        maior = galera[-1]
        menor = galera[-1]
    dados.append(galera[:])
    galera.clear()
    totpessoas += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for p in dados:
    if p[1] > maior:
        maior = p[1]
        pesomaior.clear()
        pesomaior.append(p[0])
    elif p[1] == maior:
        pesomaior.append(p[0])
    if p[1] < menor:
        menor = p[1]
        pesomenor.clear()
        pesomenor.append(p[0])
    elif p[1] == menor:
        pesomenor.append(p[0])

print(f"Ao todo, você cadastrou {totpessoas} pessoas.")
print(f"O maior peso foi de {maior}Kg. Peso de {pesomaior}")
print(f"O menor peso foi de {menor}Kg. Peso de {pesomenor}")
