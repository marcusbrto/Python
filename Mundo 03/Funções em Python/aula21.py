def fatorial(num = 1):
    """
    -> Calcula a fatorial de um numero
    :param num: pega o valor e mostra o fatorial de um numero
    :return: resultado da fatorial de um numero
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")
help(fatorial)