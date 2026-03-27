num = int(input("Digite um número inteiro: "))
escolha = str(input("Digite uma das bases para conversão:\n "
                    "[ 1 ] Binário\n "
                    "[ 2 ] Octal\n "
                    "[ 3 ] Hexadecimal\n"
                    "Sua opção: "))

if escolha == "1":
    binario = bin(num)[2:]#esses [2:] é para tirar o prefixo na frente, texto[inicio:fim]
    print(f"Seu número {num} em binário é {binario}.")
elif escolha == "2":
    octal = oct(num)[2:]
    print(f"Seu número {num} em octal é {octal}.")
elif escolha == "3":
    hexadecimal = hex(num)[2:]
    print(f"Seu número {num} em hexadecimal é {hexadecimal}.")
else:
    print("Opção invalida. Tente novamente.")


