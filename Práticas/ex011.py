
idade = int(input("Qual a sua idade? "))
preco = 20

if idade >= 60:
    preco += preco / 2
    print(f"Por conta da idade você paga meia-entrada! Valor: R${preco:.2f}")
elif idade >= 18:
    print(f"O valor da entrada é de R${preco}")
else:
    print("Menor de idade NÃO pode entrar")