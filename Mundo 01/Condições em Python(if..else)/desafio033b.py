n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print("\033[35mO número {} é o maior!\033[m".format(maior))
print("\033[34mO número {} é o menor!\033[m".format(menor))
