num = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in num: #verifica se não já não tem o valor na lista
        num.append(n) #se não tiver ele vai adicionar
        print("Valor adicionado com sucesso!")
    else: #se tiver ele manda um aviso e não faz nada
        print("Valor duplicado! Não vou adicionar")
    r = str(input("Quer continuar? [S/N] ")).lower().strip()[0]
    if r in "n":
        break
print("-="*30)
print(f"Você digitou os valores {sorted(num)}")