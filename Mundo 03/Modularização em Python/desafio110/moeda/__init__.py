def aumentar(valor = 0, porcentagem = 0,formatado=False):
    res = valor + (valor * porcentagem/100)
    return res if formatado == False else moeda(res)

def diminuir(valor = 0, porcentagem = 0,formatado=False):
    res = valor - (valor * porcentagem/100)
    return res if formatado == False else moeda(res)

def dobro(valor = 0,formatado=False):
    res = valor * 2
    return res if formatado == False else moeda(res)

def metade(valor = 1,formatado=False):
    res = valor / 2
    return res if formatado == False else moeda(res)

def moeda(valor = 0,moeda = 'R$'):
    return f"{moeda}{valor:>.2f}".replace('.',',')

def resumo(valor = 0, porcetagem = 0,dimPorcetagem = 0,formatado=False):
    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)
    print(f"Preço analisado: \t\t{moeda(valor)}")
    print(f"O dobro do preço: \t\t{moeda(dobro(valor))}")
    print(f"A metade do preço: \t\t{moeda(metade(valor))}")
    print(f"Com {porcetagem}% de aumento:\t\t{aumentar(valor,porcetagem, True)}")
    print(f"Com {dimPorcetagem}% de desconto:\t{aumentar(valor, porcetagem, True)}")
    print("-"*40)

