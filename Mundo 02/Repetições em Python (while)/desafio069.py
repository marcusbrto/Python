maioridade = 0
homens = 0
mulhermenor = 0
print(30 * "-")
print("     CADASTRE UMA PESSOA  ")
while True:
    print(30 * "-")
    idade = int(input("Idade: "))
    if idade >= 18:
        maioridade += 1
    sexo = str(input("Sexo [M/F]: ")).lower().strip()
    while sexo != "m" and sexo != "f":
        sexo = str(input("Sexo [M/F]: ")).lower().strip()
    if sexo == "m":
        homens += 1
    elif sexo == "f" and idade < 20:
        mulhermenor += 1
    print(30 * "-")
    continuar = str(input("Quer continuar? [S/N]")).strip().lower()
    while continuar != "s" and continuar != "n":
        continuar = str(input("Quer continuar? [S/N]")).strip().lower()
    if continuar == "n" :
        break
print(30 * "-")
print(f"O total de pessoas com mais de 18 anos: {maioridade}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulhermenor} mulheres com menos de 20 anos")
print(30 * "-")