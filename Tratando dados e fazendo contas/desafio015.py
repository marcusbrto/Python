dias = int(input("Quantos dias alugados? "))
kms = int(input("Quantos km rodados? "))
valor_total = (dias * 60) + (kms * 0.15)
print("O total a pagar é de R${}".format(valor_total))