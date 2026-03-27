print("{:=^40}".format("LOJAS MARCOLA"))
preco = float(input("Preço das compras: R$"))
print(''''Formas de pagamento"
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ou mais''')
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco / 2
    print(f"O valor de {preco} em 2x fica em parcelas de {total:.2f} SEM JUROS.")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"O valor de {preco} em {totparc}x fica em parcelas COM JUROS no valor de R${parcela:.2f}.")
else:
    total = 0 #total tem que receber zero se não da erro
    print("\033[41mOpção inválida, tente novamente.\033[m")
print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")