lista = list()
for c in range(0,5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]: #se for o primeiro número adicionado OU o numero maior que o ultimo ele adiciona no final
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print("-="*30)
print(f"Os valores digitados em ordem foram {lista}")