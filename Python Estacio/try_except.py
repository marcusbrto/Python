try:
    numero = int(input("Digite um número: "))
    print(10 / numero) 
except ZeroDivisionError: 
    print("Não é possível dividir por zero.")