def fatorial(num=1, mostrar=False):
    """
    -> fatorial(num=1, mostrar=False)
    -> Calcula o fatorial de um número
    :param num: número a ser calculado
    :param mostrar: se True, mostra o cálculo; se False, não mostra
    :return: valor do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if mostrar:
            print(f"{c}", end=" x " if c > 1 else " ")
        f *= c
    return f


n = int(input("Digite um número: "))

while True:
    resp = input("Deseja ver o cálculo? [S/N] ").strip().upper()[0]
    if resp in "SN":
        break

mostrar = True if resp == "S" else False

print(f"\nO fatorial de {n} é {fatorial(n, mostrar)}")

