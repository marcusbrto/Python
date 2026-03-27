numero = int(input("Digite um número para ver sua tabuada: "))
print("=" * 30)
for c in range(1,11):
    print(f"{numero} x {c} = {numero*c}")
print("=" * 30)