import time  # Biblioteca para usar pausas com sleep


def linha():
    print('-=' * 20)  # Linha decorativa


def contagem_simples():
    linha()
    print("Contagem de 1 até 10 de 1 em 1.")
    for c in range(1, 11):
        print(f'{c} ', end='')
        time.sleep(0.5)
    print("FIM!")


def contagem_regressiva():
    linha()
    print("Contagem de 10 até 0 de 2 em 2.")
    for c in range(10, -1, -2):
        print(f'{c} ', end='')
        time.sleep(0.5)
    print("FIM!")


def contagem_personalizada():
    linha()
    print("CONTAGEM PERSONALIZADA")

    ini = int(input("Inicio: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))

    if passo == 0:
        print("Passo inválido!")
        return  # Encerra a função se o passo for inválido

    # Ajusta automaticamente o sinal do passo
    if ini > fim:
        passo = -abs(passo)
    else:
        passo = abs(passo)

    for c in range(ini, fim + (1 if passo > 0 else -1), passo):
        print(f'{c} ', end='')
        time.sleep(0.5)

    print("FIM!")


# Programa principal
contagem_simples()
contagem_regressiva()
contagem_personalizada()
linha()
