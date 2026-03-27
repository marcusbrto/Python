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

