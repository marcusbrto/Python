num = list()
pares = list()
impares = list()
for c in range(0, 7):
    num.append(int(input(f"Digite o {c+1} valor: ")))
    if num[c] % 2 == 0:
        pares.append(num[c])
    else:
        impares.append(num[c])
pares = sorted(pares)
impares = sorted(impares)
print(f"Os valores pares digitados fora: {pares}")
print(f"Os valores ímpares digitados fora: {impares}")
