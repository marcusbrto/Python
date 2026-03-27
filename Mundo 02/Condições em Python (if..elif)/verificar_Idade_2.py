idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade Inválida")
    exit()

if idade >= 18:
    print("Acesso permitido.")

else:
    print("Acesso Negado.")