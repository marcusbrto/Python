def maior(*num):
    print('-='*40)
    print('Analisando os valores passados...')
    print(f"{num} Foram informados {len(num)} valores ao todo.")
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print(f"O maior valor informado foi {maior}")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()