def aumentar(valor = 0, porcentagem = 0):
    return valor + (valor * porcentagem/100)

def diminuir(valor = 0, porcentagem = 0):
    return valor - (valor * porcentagem/100)

def dobro(valor = 0):
    return valor * 2

def metade(valor = 0):
    return valor / 2

def moeda(valor = 0, moeda = 'R$'):
    valorformatado = f"{valor:.2f}"
    valorformatado = valorformatado.replace('.', ',')
    return "R$" + valorformatado

