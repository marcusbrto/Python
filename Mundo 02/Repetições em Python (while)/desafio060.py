fatorial = resultado = 0
f = 1

num = int(input("Digite um número para mostrar seu fatorial: "))

while num >= 1:
    resultado = f * num
    num = num - 1
    print(resultado)
print(f"\nO fatorial do número {num} é {resultado}")

