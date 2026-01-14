nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
print(f"A média de {nota1} e {nota2} foi de {media}.")

if media < 5:
    print("Reprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Aprovado")