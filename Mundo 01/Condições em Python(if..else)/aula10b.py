n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media >= 7: #if = se
    print("Aprovado")
elif media >= 5:#elif = senao se
    print("Em recuperação")
else: #else = senao , ele não recebe condição só faz o que sobrou
    print("Reprovado")
print("Fim")