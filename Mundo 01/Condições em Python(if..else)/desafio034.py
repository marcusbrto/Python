salario = float(input("Digite seu salário: "))
if salario >= 1250:
    valor = salario + (salario * 10 / 100)
    print("Seu novo salário é de R${}!".format(valor))
else:
    valor = salario + (salario * 15 / 100)
    print("Seu novo salário é de R${}!".format(valor))