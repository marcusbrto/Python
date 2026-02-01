pessoas = dict()
grupo = list()
mulheres = list()
idade = soma = numpessoas = 0
while True:
    nome = str(input("Nome: "))
    pessoas["nome"] = nome
    sx = str(input("Sexo: [M/F] ")).upper().strip()[0]
    while sx not in "MF":
        print("Erro! Digite apenas M ou F.")
        sx = (str(input("Sexo: [M/F] "))).upper().strip()[0]
    pessoas["sexo"] = sx
    if sx == "F":
        mulheres.append(nome)
    idade = int(input("Idade: "))
    pessoas["idade"] = idade
    soma += idade
    grupo.append(pessoas.copy())
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while continuar not in "SN":
        print("Erro! Digite apenas S ou N.")
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    numpessoas += 1
    if continuar == "N":
        break
print("-_"*40)
print(f"A) Ao todo temos {numpessoas} pessoas cadastradas.")

media = soma / numpessoas

print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram {mulheres}")

print(f"D) Lista das pessoas que estão acima da média:")
for p in grupo:
    if p["idade"] > media:
        print(f" nome = {p["nome"]} sexo = {p["sexo"]} idade = {p["idade"]};")

print("ENCERRADO")