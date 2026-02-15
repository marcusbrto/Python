def resumo(valor,aumPorcentagem,diminPorcentagem):
    def aumentar(valor, aumpPorcentagem):
        valormaior = valor + (valor * aumPorcentagem / 100)
        return valormaior
    def diminuir(valor, diminPorcentagem):
        valormenor = valor - (valor * diminPorcentagem / 100)
        return valormenor
    def dobro(valor):
        valordobro = valor * 2
        return valordobro
    def metade(valor):
        valormetade = valor / 2
        return valormetade
    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)
    print(f"Preço analisado:        R${valor:.2f}".ljust(45))
    print(f"Dobro do preço:         R${dobro(valor):.2f}".ljust(45))
    print(f"Metade do preço:        R${metade(valor):.2f}".ljust(45))
    print(f"{aumPorcentagem}% de aumento:         R${aumentar(valor, aumPorcentagem):.2f}".ljust(45))
    print(f"{diminPorcentagem}% de redução:         R${diminuir(valor, diminPorcentagem):.2f}".ljust(45))
    print("-"*40)

