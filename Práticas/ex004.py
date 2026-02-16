lista = list()

for c in range(1,4):
    num = int(input(f"Numero {c}: "))
    if c == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    lista.append(num)

print(f"Lista completa: {lista}")
print(f"O maior numero foi {maior} e o menor {menor}")
