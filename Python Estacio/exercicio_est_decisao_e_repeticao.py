raiz = 1

while raiz * raiz < 1000:
    raiz += 1

menor_raiz = raiz


while raiz * raiz <= 9999:
    raiz += 1

maior_raiz = raiz - 1

for raiz in range(menor_raiz, maior_raiz + 1):

    num = raiz * raiz

    menor = num % 100
    maior = num // 100

    if (maior + menor) == raiz:
        print(num)
        print(menor)
        print(maior)
        print(raiz)

print("fim")
