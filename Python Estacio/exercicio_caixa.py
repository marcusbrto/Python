item01,valor01 = "Maçã",0.50
item02,valor02 = "Banana",1.00
item03,valor03 = "Melancia",5.00
item04,valor04 = "Guarana",4.50

soma_total = 0

print(17 * "=+")
print(" EXERCICIO CAIXA DE SUPERMERCADO ")
print(17 * "=+")
print()

while True:
    print()
    print("Qual item desejas adicionar? ")
    print()
    print(f"1 - Nome: {item01}, Valor: {valor01}")
    print(f"2 - Nome: {item02}, Valor: {valor02}")
    print(f"3 - Nome: {item03}, Valor: {valor03}")
    print(f"4 - Nome: {item04}, Valor: {valor04}")
    print(f"5 - Faturar")
    print()
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        soma_total += valor01
        print(f"{item01} adicionado!")
    elif opcao == 2:
        soma_total += valor02
        print(f"{item02} adicionado!")
    elif opcao == 3:
        soma_total += valor03
        print(f"{item03} adicionado!")
    elif opcao == 4:
        soma_total += valor04
        print(f"{item04} adicionado!")
    elif opcao == 5:
        break
    else:
        print("OPÇÃO INVÁLIDA!")
        
print(f"O valor total da venda foi de R${soma_total}")