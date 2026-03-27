from random import choice
#importando uma biblioteca chamada random mas só a função choice, que é escolha
nome1 = str(input("Digite o nome do primeiro aluno: "))
nome2 = str(input("Digite o nome do segundo aluno: "))
nome3 = str(input("Digite o nome do terceiro aluno: "))
nome4 = str(input("Digite o nome do quarto aluno: ")) #cada nome fica em uma variavel diferente sem relação uma com a outra
sorteio = [nome1, nome2, nome3, nome4] #uma lista com todas as variaveis, essa parte é importante
escolhido = choice(sorteio) #aqui a função choice só faz escolher alguma variavel da lista
print("O aluno escolhido foi {}".format(escolhido)) #mostrei na tela