import datetime
menor = 0
maior = 0

for c in range (1, 8):
    ano = int(input(f"Digite o ano de nascimento N{c}: "))
    idade = datetime.date.today().year - ano
    if idade < 18:
        menor = (menor + 1)
    else:
        maior = (maior + 1)
print(f"No total foram 2010"
      f"{menor} pessoas menor de 18 anos e {maior} pessoas maiores de 18 anos.")