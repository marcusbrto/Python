largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

area = largura * comprimento

print(f"Área do terreno: {area} m²")

if area < 100:
    print("Classificação: TERRENO POPULAR")
elif area <= 500:
    print("Classificação: TERRENO MASTER")
else:
    print("Classificação: TERRENO VIP")
