primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (razao * 10)

for c in range(primeiro, decimo, razao):
    print(f"{c}", end=" ")
print("FIM")