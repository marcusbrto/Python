nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
alist = str(input("Você já se alistou?[S/N] ")).upper()

print(f"Olá {nome}!")

if idade < 18:
    falta = 18 - idade
    print(f"Você não pode se alistar, faltam {falta} anos.")
else:
    if alist == "S":
        print("Parabens, boa sorte capindo lote")
    elif alist == "N":
        falta = idade - 18
        print(f"Já podia ter se alistado a {falta} anos.")
    else:
        print("Reposta inválida. Use apenas S ou N")
