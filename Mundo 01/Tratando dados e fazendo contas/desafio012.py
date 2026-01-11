preco = float(input("Digite o valor do produto: "))
desconto = preco - (preco * 5 / 100) #esse é o calculo do desconto, se fosse um aumento era só trocar o - por +
print("O valor de R${} com desconto de 5% é de R${}.".format(preco,desconto))