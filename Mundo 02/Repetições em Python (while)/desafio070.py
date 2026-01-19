soma = cont = precomaior = 0

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1
    if cont == 1: #só para declarar as variaveis mesmo
        nomemenorpreco = produto
        precomenor = preco
    if preco < precomenor:
        precomenor = preco
        nomemenorpreco = produto
    if preco > 1000:
        precomaior += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while continuar != 'N' and continuar != 'S':
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == 'N':
        break
print("===========FIM DO PROGRAMA==========")
print(f"O total da compra foi R${soma:.2f}")
print(f"Temos {precomaior} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nomemenorpreco} que custa R${precomenor:.2f}")
