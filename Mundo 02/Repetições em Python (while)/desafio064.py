soma = 0
c = 1

while True:
    num = int(input(f"Digite o {c} valor: "))
    soma = num + soma
    total = c
    c = c + 1
    if num == 999:
        break
print(f"Foram digitados {total} números e a soma deles é {soma}")