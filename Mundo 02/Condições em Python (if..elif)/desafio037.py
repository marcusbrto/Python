num = int(input("Digite um número: "))

binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:] #esses [2:] é para tirar o prefixo na frente

print(f"Seu número {num} em binário é {binario}, em octal é {octal} e em hexadecimal é {hexadecimal}.")
