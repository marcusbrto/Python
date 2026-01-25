num = list()
pares = list()
impar = list()
while True:
    num.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] ")).upper()[0]
    if resp in "N":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)

print("-="*30)
print(f"Lista completa {num}")
print(f"Pares: {pares}")
print(f"Impar: {impar}")