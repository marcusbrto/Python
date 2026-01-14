nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
sexo = str(input("Qual seu sexo?[F/M] ")).upper()


if sexo == "F":
    print(f"Que pena {nome}, você não pode se alistar.")
elif idade < 18:
    falta = 18 - idade
    print(f"Que pena {nome}, você não pode se alistar, faltam {falta} anos.")
else:
    alist = str(input("Você já se alistou?[S/N] ")).upper()
    if alist == "S":
        print(F"Parabens {nome}, boa sorte capindo lote")
    elif alist == "N":
        falta = idade - 18
        print(f"Já podia ter se alistado a {falta} anos.")
    else:
        print("Resposta inválida. Use apenas S ou N!")
