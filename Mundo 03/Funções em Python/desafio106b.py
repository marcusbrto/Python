from time import sleep

c = ('\033[m',#sem cor
     '\033[0;30;41m',#vermelho
     '\033[0;30;42m',#verde
     '\033[0;30;43m',#amarelo
     '\033[0;30;44m',#azul
     '\033[0;30;45m',#roxo
     '\033[47m')   #branco

def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'", 4)
    print(c[6], end="")
    help(com)
    print(c[0], end="")
    sleep(1)

def titulo(msg,cor=0):
    tam = len(msg) + 8
    print(c[cor],end="")
    print('~'*tam)
    print(f'{msg.center(tam)}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)

#Programa principal
comando = ""
while True:
    titulo("SISTEMA DE AJUDA PYTHON", 2)
    comando = str(input("\033[mFunção ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!",1)