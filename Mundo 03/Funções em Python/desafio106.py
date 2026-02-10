def sistema(msg):
    tam = len(msg) + 34
    print("\033[44m~\033[m"*tam)
    print(f"\033[44m  ACESSANDO O MANUAL DO COMANDO {msg}  \033[m")
    print("\033[44m~\033[m"*tam)

    print(f"\033[45m{help(msg)}")


print("\033[43m~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")
print("\033[43m  SISTEMA DE AJUDA PyHELP  \033[m")
print("\033[43m~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")
funcao = str(input("\033[mFunção ou Biblioteca: "))
sistema(funcao)

