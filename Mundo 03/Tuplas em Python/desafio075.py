numnove = 0
for c in range(1,6):
    num = int(input(f"Digite o {c} valor: "))
    numtupla = (num)
    if numtupla == 0:
        numnove += 1
    if numtupla % 2 == 0:
        numpar = (numtupla)
print("FIM")
print(numtupla)
#print(f"O número 9 apareceu {numtupla.count(9)} vezes")
#print(f"O número três foi digitado primeiro na posição {numtupla.index(3)}")
#print(f"Os números pares são: {numpar}")
