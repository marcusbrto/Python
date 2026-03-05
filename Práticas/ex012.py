
quantidadeTotal = int(input("Quantos carros serão registrados? "))

for c in range(1, quantidadeTotal + 1):
    modelo = str(input("Qual o modelo do carro? "))
    anoFabricacao = int(input("Qual o ano de fabricacao? "))
    funciona = int(input("Está funcionando ( 1 ou 0 )? "))

    if anoFabricacao < 2005 and funciona == 0:
        print(f"O carro {modelo} precisa de REPAROS URGENTES!")
    elif anoFabricacao < 2005 and funciona == 1:
        print(f"O carro {modelo} é antigo, recomenda-se uma revisão")
    elif anoFabricacao >= 2005 and funciona == 0:
        print(f"O carro {modelo} precisa de manutenção!")
    elif anoFabricacao >= 2005 and funciona == 1:
        print(f"O carro {modelo} está em boas condições!")