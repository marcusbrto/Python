valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos você vai pagar?"))

tempo = anos * 12
valor_mes = valor_casa / tempo

if valor_mes > salario * 0.30:
    print("Emprestimo negado")
else:
    print(f"Emprestimo aceito, o valor mensal é de {valor_mes:.2f} por {tempo} meses. ")

