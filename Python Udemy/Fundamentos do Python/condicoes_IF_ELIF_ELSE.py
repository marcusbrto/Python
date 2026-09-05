notaSomadas = 0
qntNotas = 0

while qntNotas == 0:
    qntNotas = int(input("Serão registradas quantas notas? "))

for i in range(qntNotas):
    nota = float(input(f"Digite a {i+1} nota: "))
    notaSomadas += nota

media = notaSomadas / qntNotas

print("")
print(f"A média é \033[36m{media}\033[m")

if media >= 7: #SE
    print("\033[32mAluno aprovado!\033[m")
elif media >= 5: #SE SENÃO
    print("\033[33mAluno em recuperação\033[m")
else: #SENÃO
    print("\033[31mAluno reprovado\033[m")
