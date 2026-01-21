from random import randint
c = menor = maior = 0
for c in range(0,5):
    num_aleatorio = randint(1, 20)
    num = (num_aleatorio)
    c += 1
    if c == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print(f"{c} número gerado foi: {num}")

print("\033[32mFIM\033[m")
print(f"O maior número foi {maior} e o menor foi {menor}")