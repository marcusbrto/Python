idade = int(input("Digite sua idade: "))
carteira = str(input("Você tem carteira? [S/N] "))
seguro = str(input("Você tem seguro? [S/N] "))

if idade >= 18 and carteira == "S":
    print("Você pode dirigir!")
if seguro == "S":
    print("Pode bater a vontade")
else:
    print("Você não pode dirigir!")