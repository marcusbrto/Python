pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Responda apenas M ou F.")
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        confirmacao = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        if confirmacao in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if confirmacao == "N":
        break
print("-=" * 20)
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"A média de idade é de {media:5.2f} anos.")
print("As mulheres cadsatradas foram", end=" ")
for c in galera:
    if c["sexo"] in "F":
        print(f"{c['nome']} ", end="")
print()
print("Lista de pessoas que estão acima da média: ")
for p in galera:
    if p["idade"] >= media:
        print("  ",end="")
        for k, v in p.items():
            print(f" {k}: {v}", end=" ")
        print()
print("-=" * 20)
print("<< ENCERRADO >>")