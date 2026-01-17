c = 0
while c != 1:
    sexo = str(input("Digite seu sexo[F/M]: ")).strip().upper()[0]
    if sexo != "F" and sexo != "M":
        print("Sexo invalido, por favor digite apenas M ou F")
    else:
        if sexo == "M":
            result = "Masculino"
        else:
            result = "Feminino"
        c += 1
print(f"Seu sexo é {result}.")