# Funções matemáticas

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado
