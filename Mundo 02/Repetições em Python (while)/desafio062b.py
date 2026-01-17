print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro Termo: "))
razao =  int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termo você quer mostrar a mais? "))
print(f"Total de {total} termos mostrados.")