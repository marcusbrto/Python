altura = float(input("Qual a altura da parede em metros: "))
largura = float(input("Qual a largura da parede em metros: "))
area = altura * largura
tinta = area / 2
print("A área da sua parede é {}, será necessário {} litros de tinta.".format(area,tinta))