print("\033[0;30;41mTeste\033[m")
print("\033[4;33;44mTeste\033[m")
print("\033[1;35;43mTeste\033[m")
print("\033[30;42mTeste\033[m")
print("\033[7;33;44mTeste\033[m")
print("\033[0;40mTeste\033[m")

A = 3
B = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!".format(A,B))


nome = "Marcola"

cores = {"Limpa": "\033[m",
         "azul": "\033[34m",
         "amarelo": "\033[33m",
         "pretoebranco":"\033[7;30m"}#basicamente cria as cores

print("Olá! Muito prazer te conhecer {}{}{}!".format(cores["amarelo"], nome, cores["Limpa"]))