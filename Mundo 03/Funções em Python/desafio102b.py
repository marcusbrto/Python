def fatorial(n, mostrar=False):
    f = 1
    for c in range(n, 0, -1):
        if mostrar:
            print(c, end="")
            if c > 1:
                print( " x ", end="")
            else:
                print( " = ", end="")
        f *= c
    return f



print(fatorial(5,mostrar=True))