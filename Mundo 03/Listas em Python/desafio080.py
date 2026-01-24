lista = list()
num = 0
for c in range(0, 5):
    num = input("Digite um valor: ")
    if c == 0:
        lista.append(num)
    else:
        inseriu = False
        for i,v in enumerate(lista):
            if num < v:
                lista.insert(i,num)
                inseriu = True
                break
        if not inseriu:
            lista.append(num)


print(lista)