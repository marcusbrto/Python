from random import shuffle

nome1 = str(input("Digite o nome do primeiro aluno: "))
nome2 = str(input("Digite o nome do segundo aluno: "))
nome3 = str(input("Digite o nome do terceiro aluno: "))
nome4 = str(input("Digite o nome do quarto aluno: "))

alunos = [nome1, nome2, nome3, nome4]

shuffle(alunos)

print("A ordem de apresentação será:")
print(alunos)

