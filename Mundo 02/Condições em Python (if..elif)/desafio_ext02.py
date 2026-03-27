idade = int(input("Digite sua idade: "))
licenca = str(input("Você tem licença?[S/N] ")).upper()
seguro = str(input("Você tem seguro?[S/N] ")).upper()

if idade >= 18 and licenca == "S":
    print("Você pode dirigir")
elif seguro == "S":
    print("Você pode capotar a vontade")
else:
    print("Você não pode dirigir")