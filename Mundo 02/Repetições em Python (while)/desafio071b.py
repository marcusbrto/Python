print("=" * 30)
print("{:^30}".format("BANCO CV"))
print("=" * 30)
valor = int(input("Que valor você quer sacar? R$"))
total = valor # valor total do saque
cedula = 50 # começa sempre no maior
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1  #primeira parte do loop (entregando notas), enquanto der pra repetir com celula de 50 ele repete
    else:
        if totced > 0: #quando não da pra usar mais aquela nota
            print(f"Total de {totced} cédulas de R${cedula}")
            #aqui embaixo ele só faz as trocas
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0: #condição pra sair do while, no caso quando não tiver mais dinheiro
            break
print("=" * 30)
print("Volte sempre ao BANCO CV!")
print("=" * 30)