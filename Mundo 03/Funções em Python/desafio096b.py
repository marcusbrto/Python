def area(a,b):
    resultado = a * b
    print()
    print(f"A área de um terreno {a}x{b} é de {resultado}")

print("Controle de Terrenos")
print("-"*30)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

area(largura,comprimento)