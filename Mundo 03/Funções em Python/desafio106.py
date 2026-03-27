def ajuda(comando):
    help(comando)


#Programa principal
comando = ""
while True:
    print("\033[42m-"*30)
    print("    SISTEMA DE AJUDA PYTHON")
    print("\033[42m-"*30)
    comando = str(input("\033[mFunção ou Biblioteca >"))
    if comando.upper() == "FIM":
        print("\033[41m-" * 30)
        print(f"\033[41m    ATÉ LOGO!")
        print("\033[41m-" * 30)
        break
    else:
        print("\033[44m-"*30)
        print(f"\033[44mAcessando o manual do comando {comando}")
        print("\033[44m-"*30)
        ajuda(comando)