from random import randint
lista = list()
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
qnt = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'{f"SORTEANDO {qnt} JOGOS":=^40}')
for c in range(0, qnt):
    while len(lista) < 6:  # enquanto não tiver 6 números
        num = randint(1, 60)
        if num not in lista:  # só entra se não repetir
            lista.append(num)

    print(f"Jogo {c+1}: {lista}")
    lista.clear()
print(f'{"BOA SORTE":=^40}')