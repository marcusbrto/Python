valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
if (valor1 < valor2 + valor3) and (valor2 < valor1 + valor3) and (valor3 < valor1 + valor2):
    print("Pode formar um triângulo.")
else:
    print("Não pode formar um triângulo.")