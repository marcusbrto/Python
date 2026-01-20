total = M1000 = menor = cont = 0
barato = ""
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        M1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print("Fim do programa")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {M1000} produtos a mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")