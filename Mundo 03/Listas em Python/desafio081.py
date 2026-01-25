lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if cont == "N":
        break
print("-=" * 30)
print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não está na lista!")
