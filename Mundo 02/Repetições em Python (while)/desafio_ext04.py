soma = cont = 0
while True:
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    while True:
        confirma = str(input("Quer continuar? [S/N]")).upper().strip()[0]
        if confirma != "S" and confirma != "N":
            print("Opção invalida")
        if confirma in "SN":
            break
        print("Opção invalida, Digite apenas S ou N")
    if confirma == "N":
        break
media = soma / cont
print(f"Você digitou {cont} números")
print(f"A soma foi {soma}")
print(f"A média foi {media}")