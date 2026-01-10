from math import sin,cos,tan,radians

angulo = float(input("Digite um angulo: "))
radian = radians(angulo)
sen = sin(radian)
cos = cos(radian)
tan = tan(radian)
print("Seno:{:.2f}\nCos:{:.2f}\nTangente:{:.2f}".format(sen, cos, tan))