frase = str(input("Digite uma frase: ")).strip().upper()#upper para não dar problema de contagem com maiuscula e minuscula, strip sempre importante para tirar os espaços
contador = frase.count("A")
print("Quantidade de letras A que aparece: ",contador)
print("Aparece primeiro em {}".format(frase.find("A",0)+1)) #find faz uma busca da esquerda pra direita, nesse caso em busca de A, o +1 é porque array começa em 0 ai não confunde o usuario
print("Aparece por último em {}".format(frase.rfind("A",contador)+1))#rfind faz a busca da direita pra esquerda.
