def maiorNumero(lst):
    maior = 0
    tamLst = range(len(lst))
    for i in tamLst:
        if lst[i] > maior:
            maior = lst[i]
    print(maior)

lista = [10, 2, 5, 6, 32, 17]
maiorNumero(lista)
