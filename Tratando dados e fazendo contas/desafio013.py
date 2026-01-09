salario = float(input("Digite o salário: R$"))
aumento = salario + (salario * 15 / 100)
print("Seu salário R${} com aumento de 15% passa a ser R${:.2f}".format(salario, aumento))