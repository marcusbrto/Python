valor = float(input("Digite o valor a ser cobrado: "))
mPagamento = str(input("Qual o meio de pagamento? Cartao ou dinheiro: ")).lower()

if mPagamento == "cartao":
    parcela = str(input("Vai ser no cartão avista ou parcelado(2x)? "))
    if parcela == "parcelado":
        print(f"Preço Cartão Parcelado: {valor}")
    elif parcela == "avista":
        desconto = valor - (valor * 5/100)
        print(f"Preço Cartão Avista: {desconto}")
elif mPagamento == "dinheiro":
    desconto = valor - (valor * 10 / 100)
    print(f"Preço Dinheiro Avista: {desconto}")
else:
    print("Pagamento inválido")