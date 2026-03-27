try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print(f"O erro encontrado foi {erro}")
else:
    print(f"O resultado é {r:.2f}")
finally:
    print("\033[34mVolte sempre! :D\033[m")