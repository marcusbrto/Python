class ExcecaoCustomizada(Exception):
    pass

def checa_valor(valor1,valor2):
    if valor1 < 0 or valor2 < 0:
        raise ExcecaoCustomizada("Valor não pode ser negativo!")

def divide(a, b):
    checa_valor(a,b)
    return a / b


try:
    resultado = divide(10, 0)
except ZeroDivisionError as ex:
    print(f"Erro de divisão por zero: {ex}")

print(resultado)