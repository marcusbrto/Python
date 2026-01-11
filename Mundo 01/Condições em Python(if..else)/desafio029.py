velocidade = int(input("A qual velocidade você estava andando em km? "))
if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 7
    print("Valor: R${}".format(multa))
else:
    print("Você estava dentro do limite de velocidade.")