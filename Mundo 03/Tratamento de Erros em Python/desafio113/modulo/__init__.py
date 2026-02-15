def leiaInt(msg):
    while True:
        #pedir o valor ao usuário
        try:
            num = int(input(msg))
        except Exception as erro:
            print(f"\033[31mFoi encontrado um erro: {erro}.\033[m")
        else:
            return num

def leiaFloat(msg):

    while True:
        entrada = input(msg).strip().replace(',', '.')

        try:
            num = float(entrada)

            # verifica se é inteiro disfarçado de float
            if num.is_integer():
                raise ValueError

            return num


        except Exception as erro:

            print(f"\033[31mFoi encontrado um erro: {erro}.\033[m")

