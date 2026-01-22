numnv = 0
numt = () # tem que declarar a tupla tambem
for c in range(0,4):
    num = int(input("Digite um número: "))
    numt = numt + (num,)
    if num == 9:
        numnv += 1
print(f"O número 9 apareceu {numnv} vezes")
if 3 in numt:
    print(f"O primeiro valor 3 está na posição {numt.index(3)+1}")
print("Os números pares digitados foram: ")
for n in numt: #para cada numero dentro da tupla
    if n % 2 == 0: # se esse numero for par..
        print(n, end=" ")

