valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

#O valor de cada reta tem que ser MENOR que a soma de comprimento das outras duas retas
if (valor1 < valor2 + valor3) and (valor2 < valor1 + valor3) and (valor3 < valor1 + valor2):
    print("\033[30;42mPode formar um triângulo.\033[m")
else:
    print("\033[30;41mNão pode formar um triângulo.\033[m")