nome_entrada = input("Qual seu nome? ")
idade_entrada = input("Qual sua idade? ")

if nome_entrada and idade_entrada: #nesse caso se eles forem true, tendo algum valor  entao ele executa o codigo caso contrario ele roda o els3 que avisa que deixou vazio
    nome = str(nome_entrada)
    idade = str(idade_entrada)

    print()
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome nao contem espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, voce deixou campos vazios")
