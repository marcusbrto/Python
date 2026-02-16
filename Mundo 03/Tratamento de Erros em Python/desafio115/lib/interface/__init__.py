def leiaInt(msg):
    while True:
        #pedir o valor ao usuário
        try:
            num = int(input(msg))
        except Exception as erro:
            print(f"\033[31mFoi encontrado um erro: {erro}.\033[m")
            continue
        else:
            return num

def linha(tam = 42):
    return "-" * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}- \033[34m{item}\033[m")
        c+=1
    print(linha())
    opc = leiaInt("\033[32mSua Opção: \033[m")
    return opc

