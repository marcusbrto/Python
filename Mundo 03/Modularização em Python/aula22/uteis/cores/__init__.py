# Sistema de cores ANSI

RESET = '\033[m'
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
ROXO = '\033[35m'
CIANO = '\033[36m'
BRANCO = '\033[37m'


def colorir(texto, cor):
    return f"{cor}{texto}{RESET}"
