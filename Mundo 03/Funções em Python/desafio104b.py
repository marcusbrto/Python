def leiaInt(msg):
    while True:
        # 1) pedir o valor ao usuário
        num = input(msg).strip()

        # 2) validar se é número inteiro
        if num.isnumeric() == True:
            # 3) retornar o número convertido
            return int(num)
        else:
            # 4) mostrar mensagem de erro
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")


# Programa principal
n = leiaInt("Digite um número: ")
print(f"\033[32mVocê acabou de digitar o número {n}\033[m")
