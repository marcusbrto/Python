try:
    num = int(input("Digite um número: "))
except ValueError:
    print("\033[31mERRO! Digite um valor inteiro\033[m")
else:
    if num % 2 == 0:
        print(f"\033[32mO número {num} é PAR\033[m")
    else:
        print(f"\033[32mO número {num} é IMPAR\033[m")