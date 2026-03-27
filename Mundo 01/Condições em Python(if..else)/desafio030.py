numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("\033[35mSeu número {} é par!\033[m".format(numero))
else:
    print("\033[36mSeu número {} é impar!\033[m".format(numero))