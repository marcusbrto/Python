aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input("Media: "))
print(f"Nome: {aluno["nome"]}")
print(f"Media: {aluno["media"]}")
if aluno["media"] > 7:
    aluno["situacao"] = "Aprovado"
elif aluno["media"] > 5:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"
print(f"Situação é igual a {aluno["situacao"]}")