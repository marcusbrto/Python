import math

angulo = float(input("Digite um angulo: "))
radian = math.radians(angulo)
sen = math.sin(radian)
cos = math.cos(radian)
tan = math.tan(radian)
print("Seno:{:.3f}\nCos:{:.3f}\nTangente:{:.3f}".format(sen, cos, tan))