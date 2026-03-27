# ================================
# MÓDULO moeda.py
# Funções para cálculos e formatação de valores monetários
# ================================


def aumentar(valor=0, porcentagem=0, formatado=False):
    """
    Calcula o aumento percentual de um valor.

    Parâmetros:
    valor (float) → valor original
    porcentagem (float) → porcentagem de aumento
    formatado (bool) → se True retorna formatado em moeda

    Retorna:
    float ou string formatada
    """

    # calcula o valor com aumento
    res = valor + (valor * porcentagem / 100)

    # se formatado for False → retorna número
    # se formatado for True → retorna string formatada em moeda
    return res if formatado == False else moeda(res)


def diminuir(valor=0, porcentagem=0, formatado=False):
    """
    Calcula o desconto percentual de um valor.
    """

    # calcula o valor com desconto
    res = valor - (valor * porcentagem / 100)

    # retorna número ou moeda formatada
    return res if formatado == False else moeda(res)


def dobro(valor=0, formatado=False):
    """
    Calcula o dobro de um valor.
    """

    # multiplica por 2
    res = valor * 2

    # retorna número ou moeda formatada
    return res if formatado == False else moeda(res)


def metade(valor=0, formatado=False):
    """
    Calcula a metade de um valor.
    """

    # divide por 2
    res = valor / 2

    # retorna número ou moeda formatada
    return res if formatado == False else moeda(res)


def moeda(valor=0, moeda='R$'):
    """
    Formata um valor como moeda brasileira.

    Exemplo:
    10 → R$10,00
    """

    # :.2f → duas casas decimais
    # replace troca . por , (padrão brasileiro)
    return f"{moeda}{valor:.2f}".replace('.', ',')


def resumo(valor=0, porcetagem=0, dimPorcetagem=0, formatado=False):
    """
    Mostra um resumo completo do valor,
    incluindo dobro, metade, aumento e desconto.
    """

    # linha decorativa
    print("-" * 40)

    # título centralizado
    print("RESUMO DO VALOR".center(40))

    # linha decorativa
    print("-" * 40)

    # mostra o valor original formatado
    print(f"Preço analisado: \t\t{moeda(valor)}")

    # mostra o dobro
    print(f"O dobro do preço: \t\t{moeda(dobro(valor))}")

    # mostra a metade
    print(f"A metade do preço: \t\t{moeda(metade(valor))}")

    # mostra aumento
    print(f"Com {porcetagem}% de aumento:\t\t{aumentar(valor, porcetagem, True)}")

    # mostra desconto (corrigido)
    print(f"Com {dimPorcetagem}% de desconto:\t{diminuir(valor, dimPorcetagem, True)}")

    # linha decorativa
    print("-" * 40)
