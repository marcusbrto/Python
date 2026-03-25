print("=========================")
print("Calculadora com While :D ")
print("=========================")

while True:
    num1 = input("Digite o primeiro numero: ")
    num2 = input("Digite o segundo numero: ")
    operador = input("Digite o operador[+-/*]: ")
    operador = operador.upper()
    if operador == "S":
        break

    try:
        numero1 = int(num1)
        numero2 = int(num2)
        if operador == "+":
            print(f"A soma de {numero1} e {numero2} é {numero1 + numero2}")
        elif operador == "-":
            print(f"A subtração de {numero1} e {numero2} é {numero1 - numero2}")
        elif operador == "/":
            print(f"A divisão de {numero1} e {numero2} é {numero1 / numero2:.2f}")
        elif operador == "*":
            print(f"A multiplicação de {numero1} e {numero2} é {numero1 * numero2}")
        else:
            print("Digite um operador válido!")
    except:
        print("ERRO! Valor incorreto")

    sair = input("Deseja continuar?[S/N] ").lower().startswith('n')
    
    if sair is True:
        break