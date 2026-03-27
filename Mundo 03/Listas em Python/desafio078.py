valores = maior = menor = list()
for c in range(0, 5):
    valores.append(int(input(f"Digite o {c + 1} valor: ")))
    num = valores[c]
    if c == 0:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f"Voce digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} na posição {valores.index(maior)+1}...")
print(f"O menor valor digitado foi {menor} na posição {valores.index(menor)+1}...")
