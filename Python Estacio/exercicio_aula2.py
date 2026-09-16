def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado


def soma(num1, num2):
    resultado = num1 + num2
    return resultado


def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado


def divisao(num1, num2):
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = num1 / num2
        return resultado


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f"Subtração: {subtracao(numero1,numero2)}")
print(f"Soma: {soma(numero1,numero2)}")
print(f"Multiplicação: {multiplicacao(numero1,numero2)}")
print(f"Divisão: {divisao(numero1,numero2)}")
