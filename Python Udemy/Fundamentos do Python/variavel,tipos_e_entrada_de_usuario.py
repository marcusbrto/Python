nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (Ex: 1.80): "))
fruta_favorita = str(input("Qual sua fruta favorita? "))

ativo = str(input("O cadastro está ativo?(S/N): "))
if ativo == "S":
    valorAtivo = True
else:
    valorAtivo = False

print(f"Seu nome é {nome}, sua idade é {idade}, sua altura é {altura:.2f}, sua fruta favorita é {fruta_favorita} e cadastro ativo igual a {valorAtivo}!")
