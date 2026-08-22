num1 = 10
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

# print("Desconto: ")
# preco = float(input("Digite o preço: "))
# desconto = float(input("Digite a porcetagem de desconto: "))

# valor_liquido = preco - (preco * desconto) / 100
# print(f"O valor de {preco:.2f} com {desconto:.2f} de desconto é {valor_liquido:.2f}")

produto = int(input("Digite a quantidade do produto: "))
porcao = float(input("Digite sua porção diária de consumo desse produto: "))

dias = produto // porcao
print(f"{produto} de produtos com {porcao:.2f} de porção por dia, o produto vai durar por {dias:.0f} dias.")