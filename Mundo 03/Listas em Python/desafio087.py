lista = list()
soma = maior = 0
for c in range(0, 3):
    lista.append(int(input(f"Digite um valor para [0, {c}]: ")))
for c in range(0, 3):
    lista.append(int(input(f"Digite um valor para [1, {c}]: ")))
for c in range(0, 3):
    lista.append(int(input(f"Digite um valor para [2, {c}]: ")))

print("-=" * 30)
print(f"[ {lista[0]} ][ {lista[1]} ][ {lista[2]} ]")
print(f"[ {lista[3]} ][ {lista[4]} ][ {lista[5]} ]")
print(f"[ {lista[6]} ][ {lista[7]} ][ {lista[8]} ]")
print("-=" * 30)

for p in lista:
    if p % 2 == 0:
        soma += p

for p in lista[3:6]:
    if p > maior:
        maior = p

somacol = lista[2] + lista[5] + lista[8]

print(f"A soma dos valores pares é {soma}")
print(f"A soma da terceira coluna é {somacol}")
print(f"O maior valor da segunda linha é {maior}")

