from ContaCliente import ContaCliente


class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def calculoRendimento(self):  # (3)
        self.valor_investido += self.valor_investido * self.taxa_rendimento
