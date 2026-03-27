from random import randint

def sorteia():
    sorteado = []
    for c in range(5):
        sorteado.append(randint(0, 9))
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in sorteado:
        print(c, end=' ')
    return sorteado

def somaPar(num):
    soma = 0
    for numero in num:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros = sorteia()
resultado = somaPar(numeros)
print(f'\nSomando os valores pares temos {resultado}')

