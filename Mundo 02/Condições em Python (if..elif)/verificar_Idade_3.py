idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade Inválida")

elif idade >= 18:
    print("Acesso permitido.")

else:
    print("Acesso Negado.")