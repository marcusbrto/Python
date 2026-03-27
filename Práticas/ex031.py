"""Calculadora com while"""

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando sua operação...")
    if operador == '+':
        print(f"A soma dos numeros {num_1_float} e {num_2_float} é {num_1_float + num_2_float}")
    elif operador == '-':
        print(
            f"A subtração dos numeros {num_1_float} e {num_2_float} é {num_1_float - num_2_float}"
        )
    elif operador == '/':
        print(
            f"A divisão dos numeros {num_1_float} e {num_2_float} é {num_1_float / num_2_float}"
        )
    elif operador == '*':
        print(
            f"A multiplicação dos numeros {num_1_float} e {num_2_float} é {num_1_float * num_2_float}"
        )
    else:
        print("ERRO!")

    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break
