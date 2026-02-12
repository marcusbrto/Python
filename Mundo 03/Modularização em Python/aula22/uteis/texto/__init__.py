# Funções para manipulação de texto

def linha(tam=30):
    return "-" * tam

def titulo(msg):
    print(linha())
    print(msg.upper())
    print(linha())

def centralizar(msg, largura=30):
    return msg.center(largura)

def contar_letras(msg):
    return len(msg)
