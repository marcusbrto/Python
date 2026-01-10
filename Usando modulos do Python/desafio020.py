import random

nome1 = input("Digite o nome do primeiro aluno: ")
nome2 = input("Digite o nome do segundo aluno: ")
nome3 = input("Digite o nome do terceiro aluno: ")
nome4 = input("Digite o nome do quarto aluno: ")

alunos = [nome1, nome2, nome3, nome4]

random.shuffle(alunos)

print("A ordem de apresentação será:")
print(alunos)

