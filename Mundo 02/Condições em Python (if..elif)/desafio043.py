altura = float(input("Digite sua altura(M): "))
peso = float(input("Digite o seu peso(KG): "))

imc = peso / (altura * altura)
print(f"\033[32mIMC:{imc:.1f} \033[m")
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")