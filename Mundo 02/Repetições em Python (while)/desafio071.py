print("=" * 40)
print("           BANCO DO MARCOLA          ")
print("=" * 40)
valor = 0
while valor <= 0:
    valor = int(input("Que valor você quer sacar? R$"))
    if valor <= 0:
        print("Valor Inválido!")
valor50 = valor // 50
valorconversao50 = valor % 50
valor20 = valorconversao50 // 20
valorconversao20 = valorconversao50 % 20
valor10 = valorconversao20 // 10
valorconversao10 = valorconversao20 % 10
valor1 = valorconversao10 // 1
if valor50 > 0:
    print(f"Total de {valor50} cédulas de R$50")
if valor20 > 0:
    print(f"Total de {valor20} cédulas de R$20")
if valor10 > 0:
    print(f"Total de {valor10} cédulas de R$10")
if valor1 > 0:
    print(f"Total de {valor1} cédulas de R$1")
print("=" * 40)
print("Volte sempre ao BANCO DO MARCOLA! Tenha um bom dia!")
