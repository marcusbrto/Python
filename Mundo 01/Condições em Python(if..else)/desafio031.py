distancia = int(input("Digite a distância da viagem em KM: "))
if distancia <= 200:
    valor = distancia * 0.50
    print("Valor: R${}".format(valor))
else:
    valor = distancia * 0.45
    print("Valor: R${}".format(valor))

    # versão simplificado
'''preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("Valor: R${}".format(preco))'''