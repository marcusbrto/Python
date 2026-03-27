while True:
    c = 0 #importante que a variavel seja declarada dentro da repetição para ele reiniciar toda vez
    num = int(input("Quer ver a tabuada de qual valor? "))
    if num <= 0: break
    while c <= 10:
        print(f"{num} x {c} = {num * c}")
        c += 1

print("Programa de tabuada encerrado, volte sempre!")