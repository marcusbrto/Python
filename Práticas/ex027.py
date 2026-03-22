nome = input("Digite seu nome: ")

if nome:
    tamanho_nome = len(nome)
    if tamanho_nome >= 6:
        print("Seu nome é muito grande")
    elif tamanho_nome >= 5 and tamanho_nome < 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é curto")
else:
    print("Digite alguma coisa")
