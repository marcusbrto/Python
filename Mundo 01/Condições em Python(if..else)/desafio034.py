salario = float(input("Digite seu salário: "))
if salario >= 1250:
    valor = salario + (salario * 10 / 100)
    print("\033[30;42mSeu novo salário é de R${}\033[m!".format(valor))
else:
    valor = salario + (salario * 15 / 100)
    print("\033[30;42mSeu novo salário é de R${}!\033[m".format(valor))