def media(*notas):
    med = sum(notas) / len(notas)
    return med


qntNotas = int(input("Quantas notas vão ser adicionadas? "))

notas = []

for i in range(qntNotas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)


resultado = media(*notas)

print(f"A média foi: {resultado}")
