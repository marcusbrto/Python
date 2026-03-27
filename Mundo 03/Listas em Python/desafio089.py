turma = list()
aluno = list()
soma = 0
while True:
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    aluno.append((aluno[1] + aluno[2])/2)
    turma.append(aluno[:])
    aluno.clear()
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if continuar in "N":
        break


print("-="*30)
print("Nu.   NOME      MÉDIA")
print("-"*30)
for c in range(0, len(turma)):
    print(f"{c}{turma[c][0]:^15}{turma[c][3]:^5}")
print("-"*30)
while True:
    v = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if v == 999:
        break
    else:
        print(f"As notas de {turma[v][0]} é {turma[v][1]} e {turma[v][2]:^5}")