resp = "S"
soma = qnt = media = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    qnt += 1
    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
media = soma / qnt
print(f"Você digitou {num} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
