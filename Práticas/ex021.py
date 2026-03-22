nome_entrada = input("Qual seu nome? ")
idade_entrada = input("Qual sua idade? ")

if nome_entrada == "" or idade_entrada == "":
    print("Desculpe, voce deixou campos vazios")
else:
    nome = str(nome_entrada) 
    idade = str(idade_entrada)
    nome_invertido = nome_entrada[::-1]

    print()
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    if " " in nome_entrada:
        print("Seu nome contem espaços")
    else:
        print("Seu nome nao contem espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")

