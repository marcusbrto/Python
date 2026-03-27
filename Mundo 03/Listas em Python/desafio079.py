valor = list()
while True:
    num = int(input("Digite um valor: "))
    if num in valor: #verifica se existe na lista
        print("Valor duplicado! O número não será adicionado.")#avisa e não faz nada
    else:
        valor.append(num)
        print("Valor adicionado com sucesso...")
    cont = str(input("Deseja continuar? [S/N] ")).upper().split()[0]
    if cont != "N" and cont != "S":
        print("Digite apenas S ou N!!!")
    elif cont == "N":
        break

print("-"*30)
print(f"Você digitou os valores {valor}")