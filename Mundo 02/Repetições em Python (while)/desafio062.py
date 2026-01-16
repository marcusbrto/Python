while True: #com true não depende de uma condição já que ele sempre vai ser true até ter um break
    primeiro = int(input("\nPrimeiro termo: "))
    razao = int(input("Razão: "))
    termo = int(input("Quantos termos (digite 0 para sair): "))

    c = 1 #importante ser dentro do while para reset do contador a cada rodada

    while c <= termo:
        print(f"{primeiro} ", end="")
        primeiro += razao
        c = c + 1
    if termo == 0:
        print("\nO programa será encerrado..")
        break