numeros = [3,8,15,22,7,10]
soma = 0

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
    else:
        soma += numero
        
print(f"A soma dos valores IMPARES é: {soma}")