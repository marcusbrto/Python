
num = (int(input("Digite um número: ")),
int(input("Digite outro número: ")),
int(input("Digite mais um número: ")),
int(input("Digite o último número: ")))
print(f"Você digitou os valores{num}") #todos esses valores já estão dentro de uma tupla
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num: #esse if é necessario pois o index depende que tenha o valor que ele ta procurando, se não tiver nada da erro
    print(f"A posição do valor 3 é {num.index(3)+1} lugar")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram ",end="")
for num in num:
    if num % 2 == 0:
        print(num, end=' ')