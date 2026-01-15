soma = 0
cont = 0
for c in range(0,6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma = (soma + num)
        cont = cont + 1
print(f"Você informou {cont} números pares e a soma de todos eles é {soma}")