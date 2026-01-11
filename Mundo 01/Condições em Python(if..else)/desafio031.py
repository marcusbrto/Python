distancia = int(input("Digite a distância da viagem em KM: "))
if distancia <= 200:
    valor = distancia * 0.50
    print("Valor: R${}".format(valor))
else:
    valor = distancia * 0.45
    print("Valor: R${}".format(valor))