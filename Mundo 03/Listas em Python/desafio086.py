lista = list()
for c in range(0, 3):
    lista.append(int(input(f"Digite um valor para [0, {c}]: ")))
for c in range(0, 3):
    lista.append(int(input(f"Digite um valor para [1, {c}]: ")))
for c in range(0, 3):
    lista.append(int(input(f"Digite um valor para [2, {c}]: ")))

print("-=" * 30)
print(f"{f"[ {lista[0]} ][ {lista[1]} ][ {lista[2]} ]":^25}")
print(f"{f"[ {lista[3]} ][ {lista[4]} ][ {lista[5]} ]":^25}")
print(f"{f"[ {lista[6]} ][ {lista[7]} ][ {lista[8]} ]":^25}")