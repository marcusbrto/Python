qntvalor = 0 #esses dois é só para declarar a variavel
totalvalor = 0

while True:
    valor = int(input("Digite um valor: "))
    totalvalor += valor #variavel para guardar todos os valores para calcular a media depois
    qntvalor = qntvalor + 1 #serve para declarar as variaveis abaixo e tambem saber a quantidade de valores que foram adicionados para calcular a media depois

    if qntvalor == 1: # serve somente para declarar a variavel, fazendo com que elas recebam o primeiro valor digitado
        maior = valor
        menor = valor

    if valor > maior: # se o valor digitado for maior que o valor que já existem na variavel maior ele recebe o novo valor maior
        maior = valor
    if valor < menor:#mesma logica do maior
        menor = valor

    conf = str(input("Deseja continuar? [S/N]")).upper().strip()[0] #essas tres linhas são para encerrar o programa caso digite N
    if conf == "N":
        break

print(f"O maior valor foi {maior} e o menor foi {menor}.")

media = totalvalor / qntvalor #calcular a media de todos os valores

print(f"E a média entre todos os valores é {media:.2f}")