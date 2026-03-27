mulher_menor = 0
soma = 0
idade_velho = 0
nome_velho = ''
#variaveis que precisa declarar, enfase no nome_velho que ficou vazio para receber o nome depois

for c in range(1,5):
    nome = str(input("Digite o nome: ")).upper()
    idade = int(input("Digite sua idade: "))

    soma += idade #recebe todas as idades para fazer a media depois

    sexo = str(input("Digite o sexo:[F/M] ")).upper()
    print("=" * 40)

    if sexo == "F" and idade < 20: # aqui quantas mulheres são menor de 20 anos
        mulher_menor =+ 1

    elif sexo == "M" and idade > idade_velho: #nisso aqui ele pega a idade e nome do homem mais velho
        idade_velho = idade
        nome_velho = nome

media = soma / 4 #calcula a media normal

print(f'''A média de todas as idades é {media} anos
Existem {mulher_menor} mulheres com menos de 20 anos.
O nome do homem mais velho é {nome_velho} e sua idade é {idade_velho}''')

print("=" * 40)