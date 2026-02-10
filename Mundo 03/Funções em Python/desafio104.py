def leiaInt(msg):
    while True:
        num = input(msg).strip()
        if num.isnumeric():
            return int(num)
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")

# Programa principal
n = leiaInt("Digite um número: ")
print(f"\033[32mVocê acabou de digitar o número {n}\033[m")

