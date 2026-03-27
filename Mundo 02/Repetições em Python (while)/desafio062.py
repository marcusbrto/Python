# Inicia um loop infinito (o programa só para quando encontrar um "break")
while True:

    # Pede ao usuário o primeiro termo da PA e transforma em número inteiro
    primeiro = int(input("\nPrimeiro termo: "))

    # Pede ao usuário a razão da PA e transforma em inteiro
    razao = int(input("Razão: "))

    # Contador que vai controlar quantos termos já foram exibidos
    c = 1

    # Quantidade inicial de termos que queremos mostrar
    termo = 10

    # Enquanto o contador for menor ou igual a 10, o loop continua
    while c <= termo:

        # Mostra o termo atual na mesma linha (sem pular linha)
        print(f"{primeiro} ", end="")

        # Calcula o próximo termo da PA
        primeiro += razao

        # Aumenta o contador em 1
        c = c + 1

    # Depois de mostrar os 10 primeiros termos,
    # pergunta quantos termos a mais o usuário quer ver
    mais = int(input("\nQuantos termos você quer mostrar a mais? "))

    # Se o usuário digitar 0, o programa encerra
    if mais == 0:
        print("\nO programa será encerrado..")
        break   # Sai do while True e finaliza o programa

    # Enquanto ainda houver termos extras para mostrar...
    while mais != 0:

        # Mostra o próximo termo da PA
        print(f"{primeiro} ", end="")

        # Calcula o próximo termo
        primeiro += razao

        # Diminui a quantidade de termos restantes
        mais -= 1
