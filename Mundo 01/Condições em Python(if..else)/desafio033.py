n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 >= n2 and n1 >= n3:
    print("\033[32mO número {} é o maior!\033[m".format(n1))
elif n2 >= n3 and n2 >= n1:
    print("\033[32mO número {} é o maior!\033[m".format(n2))
else:
    print("\033[32mO número {} é o maior!\033[m".format(n3))

if n1 <= n2 and n1 <= n3:
    print("\033[33mO número {} é o menor!\033[m".format(n1))
elif n2 <= n3 and n2 <= n1:
    print("\033[33mO número {} é o menor!\033[m".format(n2))
else:
    print("\033[33mO número {} é o menor!\033[m".format(n3))