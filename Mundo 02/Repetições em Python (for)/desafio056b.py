somaidade = 0
totmulher = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''

for p in range(1, 5):
    print(f"-----{p} PESSOA-----")
    nome = str(input("Nome: ")).strip() #strip remove os espaços no começo e fim
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    somaidade += idade
    if p == 1 and sexo in "M": #o in é legal porque ele reconhece letra minuscula e maiuscula
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "F" and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho se chama {nomevelho} e sua idade é {maioridadehomem} anos.")
print(f"Ao todo são {totmulher} mulheres com menos de 20 anos.")