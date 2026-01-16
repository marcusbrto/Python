primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
c = 1

while c <= 10:
    print(f"{primeiro} ", end="")
    primeiro += razao
    c = c + 1
