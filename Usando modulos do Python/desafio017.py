from math import hypot
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)
print("A hipotenusa é {:.2f}".format(hipotenusa))