velocidade = int(input("A qual velocidade você estava andando em km? "))
if velocidade > 80:
    print("\033[1;31mVocê foi multado!\033[m")
    multa = (velocidade - 80) * 7
    print("\033[4mValor: R${}\033[m".format(multa))
else:
    print("\033[1;32mVocê estava dentro do limite de velocidade, tenha um bom dia\033[m.")