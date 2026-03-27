#metodo com pacote
"""from math import factorial
num = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(num)
print(f"O fatorial de {num} é {f}")"""

n = int(input("Digite um número para calcular o fatorial: "))
c = n
f = 1
print(f"Calculando o fatorial de {n}!")
while c > 0:
    print(f"{c}", end=" ")
    print("x" if c > 1 else " = ", end=" ")
    f = f * c
    c -= 1
print(f"{f}")