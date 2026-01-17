n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

while True:
    print("\033[1;31m[ 1 ] SOMAR\033[m")
    print("\033[1;31m[ 2 ] MULTIPLICAR\033[m")
    print("\033[1;31m[ 3 ] MAIOR\033[m")
    print("\033[1;31m[ 4 ] NOVOS NÚMEROS\033[m")
    print("\033[1;31m[ 5 ] SAIR\033[m")
    r = str(input("Qual a opção? "))
    if r == "1":
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
        print(20 * "==")
    if r == "2":
        multi = n1 * n2
        print(f"A multiplicação de {n1} * {n2} = {multi}")
        print(20 * "==")
    if r == "3":
        if  n1 > n2:
            print(f"O número {n1} é maior que {n2}")
            print(20 * "==")
        elif n1 < n2:
            print(f"O número {n2} é maior que {n1}")
            print(20 * "==")
        else:
            print(f"O número são iguais")
            print(20 * "==")
    if r == "4":
        print("Os números foram resetados!")
        print(20 * "==")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    if r == "5":
        print(20 * "==")
        print("\033[32mPrograma finalizado com sucesso!\033[m")
        print(20 * "==")
        break
    if r >= "6" or r < "1":
        print("\033[41mOpção invalida! Por favor tente novamente.\033[m")
        print(20 * "==")
