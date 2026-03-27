soma = 0
while True:
    num = int(input("Digite um número(zero para): "))
    soma += num
    if num == 0:
        break

print(f"A soma vale {soma}")