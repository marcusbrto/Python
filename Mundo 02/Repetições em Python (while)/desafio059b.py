n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

while True:
    print("""    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
    opcao = int(input(">>>>> Qual é a opção? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é igual a {soma}")
    elif opcao == 2:
        soma = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é igual a {soma}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"O número {n1} é MAIOR")
        elif n1 < n2:
            maior = n2
            print(f"O número {n2} é MAIOR")
        else:
            print(f"O número {n1} e {n2} são IGUAIS")
    elif opcao == 4:
        print("Os números serão RESETADOS, digite novamente!")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        break
    else:
        print("Opção inválida, tente novamente!")
        print("=-=" * 15)
print("Fim do programa, volte sempre!")
