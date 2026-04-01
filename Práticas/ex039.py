import os

lista = []
while True:
    print("LISTA DE COMPRAS")
    print("1 - Inserir")
    print("2 - Apagar")
    print("3 - Listar")
    print("4 - Sair")
    opcao = input("Selecione uma opcao: ")

    if opcao == "1":
        os.system("clear")
        valor = input("Valor: ")
        lista.append(valor)

    elif opcao == "2":
        indice_str = input("Escolha o índice para apagar: ")
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print("Nao foi possivel apagar este indice")
            
    elif opcao == "3":
        os.system("clear")
        
        if len(lista) == 0:
            print("Nada para listar")
            
        for i,valor in enumerate(lista):
            print(i,valor)

    elif opcao == "4":
        os.system("clear")
        print("Saindo...")
        break

    else:
        print("Opcao inválida!")