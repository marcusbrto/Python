maior = 0
menor = 9000

for c in range (1, 6):
    peso = float(input(f"Digite seu peso - N{c}: "))
    if peso >= maior:
       maior = peso
    elif peso <= menor:
        menor = peso
print("O maior peso lido foi {} e o menor peso lido foi {}".format(maior, menor))