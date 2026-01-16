c = 0

while c != 1:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("\033[1;31m[ 1 ] SOMAR\033[m")
    print("\033[1;31m[ 2 ] MULTIPLICAR\033[m")
    print("\033[1;31m[ 3 ] MAIOR\033[m")
    print("\033[1;31m[ 4 ] NOVOS NÚMEROS\033[m")
    print("\033[1;31m[ 5 ] SAIR\033[m")
    r = str(input("Qual a opção? "))
    if r == "1":
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
    if r == "2":
        multi = n1 * n2
        print(f"A multiplicação de {n1} * {n2} = {multi}")
    if r == "3":
        if  n1 > n2:
            print(f"O número {n1} é maior que {n2}")
        elif n1 < n2:
            print(f"O número {n2} é maior que {n1}")
        else:
            print(f"O número são iguais")
    if r == "4":
        print("Os números foram resetados!")
    if r == "5":
        c += 1
        print("Programa finalizado com sucesso!")
