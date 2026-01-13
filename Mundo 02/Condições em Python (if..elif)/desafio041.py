ano = int(input("Digite seu ano de nascimento: "))

idade = 2025 - ano

if idade < 9:
    print("Mirim")
elif idade > 9 and idade <= 14:
    print("Infantil")
elif idade > 14 and idade <= 19:
    print("Junior")
elif idade > 19 and idade <= 20:
    print("Sênior")
else:
    print("Master")

