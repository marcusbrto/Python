from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "arquivo.txt"

if not arquivo_existe(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver Pessoas Cadastradas","Novo Cadastro","Sair do Sistema"])
    if resposta == 1:
        cabecalho("Opção 1")
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input ("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Opção 3")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida.\033[m")
        sleep(1)