lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input("Digite um número: ")))
    if lista[-1] % 2 == 0:
        par.append(lista[-1])
    else:
        impar.append(lista[-1])
    resp = str(input("Quer continuar? [S/N] ")).upper()[0]
    if resp in "Nn":
        break

print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de impares é {impar}")