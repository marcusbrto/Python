from datetime import datetime
pessoa = {}
valor = apon = 0
pessoa["nome"] = str(input("Nome: "))
pessoa["nasc"] = int(input("Ano de nascimento: "))
idade = datetime.now().year - pessoa["nasc"]
pessoa["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if pessoa["ctps"] != 0:
    pessoa["contratacao"] = int(input("Ano de Contratação: "))
    pessoa["salario"] = float(input("Salário: R$"))
    valor += 1
    apon = pessoa["nasc"] - pessoa["contratacao"]
    apon2 = 70 - apon
else:
    pessoa["ctps"] = 0

print("-=" * 20)
print(f"nome tem o valor {pessoa['nome']}")
print(f"idade tem o valor {idade}")
print(f"ctps tem o valor {pessoa['ctps']}")
if valor != 0:
    print(f"contratacao tem o valor {pessoa['contratacao']}")
    print(f"salario tem o valor {pessoa['salario']}")
    print(f"aponsetadoria tem o valor {apon2}")