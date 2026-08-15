nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (Ex: 1.80): "))

ativo = str(input("O cadastro está ativo?(S/N): "))
if ativo == "S":
    valorAtivo = True
else:
    valorAtivo = False

print(f"Seu nome é {nome}, sua idade é {idade}, sua altura é {altura:.2f}, cadastro ativo igual a {valorAtivo}!")
