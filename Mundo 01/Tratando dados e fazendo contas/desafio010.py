real = float(input("Digite um valor real: "))
dolares = real / 5.39  #é só alterar para a contação atual
euro = real / 6.28
print("Com o valor de R${:.2f} você consegue comprar {:.2f} dólares e {:.2f} euros!".format(real,dolares,euro))