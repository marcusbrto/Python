nome = input("Digite seu nome completo: ").strip()#strip tira os espaços

partes = nome.split()#split divide em pedaços separados e organiza como lista

print("Muito prazer em te conhecer {}!".format(nome))
print("Primeiro nome:", partes[0])#peguei o primeiro da lista
print("Último nome:", partes[-1])#peguei o ultimo da lista