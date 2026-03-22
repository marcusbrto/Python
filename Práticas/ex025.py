numero = input("Digite um número inteiro: ")

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print("Número PAR")
    else:
        print("Número IMPAR")  
except:
    print("Não é um número inteiro!")
