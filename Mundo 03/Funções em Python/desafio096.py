def area(valorA,valorB):
    resultado = valorA * valorB
    return resultado

print("  CONTROLE DE TERRENOS")
print("-=" * 20)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

print(f"A área de um terreno {largura}x{comprimento} é de {area(largura,comprimento)} metros quadrados.")
