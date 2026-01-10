nome = input("Digite seu nome completo: ").strip()

partes = nome.split()

print("Primeiro nome:", partes[0])
print("Último nome:", partes[-1])