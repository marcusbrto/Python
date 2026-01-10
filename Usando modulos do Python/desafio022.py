nome = str(input("Digite seu nome completo: ")).strip() #strip tira os espaços no inicio e no final
print("Seu nome em maiusculas é: ",nome.upper())
print("Seu nome em minusculas é: ",nome.lower())
print("Quantas letras tem seu nome: ",len(nome) - nome.count(' '))
print("Quantas letras tem o primeiro nome: ",len(nome.split()[0]))