palavras = input("Digite uma palavra: ")

sem_espaco = palavras.replace(' ','')

invertida = sem_espaco[::-1]#isso inverte a palabra

if sem_espaco == invertida:
    print("É um palindromo")
else:
    print("Não é um palindromo")
