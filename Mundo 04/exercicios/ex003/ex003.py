class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques em depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.saldo = saldo
        self.titular = nome
        print(f"Conta {self.id} criada com sucesso. Saldo atual: {self.saldo}")

    def __str__(self):
        return f"A conta bancaria {self.id} de {self.titular} com saldo R${self.saldo:,.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${self.saldo:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${self.saldo:,.2f} autorizado na conta {self.id}")

c1 = ContaBancaria(112, "Marcola", 3000)
c1.sacar(2000)
print(c1)