class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adiciona_conta(self, conta_cliente):
        self.contas.append(conta_cliente)

    def calcular_rendimento_mensal(self):
        for c in self.contas:
            c.calculoRendimento()

    def imprime_saldo_contas(self):
        for c in self.contas:
            c.extrato()
