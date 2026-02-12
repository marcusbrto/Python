def aumentar(valor, porcentagem,formatado=False):
    if formatado:
        return moeda(valor + (valor * porcentagem/100))
    else:
        return valor + (valor * porcentagem/100)

def diminuir(valor, porcentagem,formatado=False):
    if formatado:
        return moeda(valor - (valor * porcentagem/100))
    else:
        return valor - (valor * porcentagem/100)

def dobro(valor,formatado=False):
    if formatado:
        return moeda(valor * 2)
    else:
        return valor * 2

def metade(valor,formatado=False):
    if formatado:
        return moeda(valor / 2)
    else:
        return valor / 2

def moeda(valor):
    valorformatado = f"{valor:.2f}"
    valorformatado = valorformatado.replace('.', ',')
    return "R$" + valorformatado

