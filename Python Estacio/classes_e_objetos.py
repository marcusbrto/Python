class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f"numero:{self.numero}\ncpf:{self.cpf}\nsaldo:{self.saldo}")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente!"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return "Transferencia Realizada!"


conta1 = Conta(123, "111.222.333-44", "Marcus", 1000)
conta2 = Conta(456, "999.888.777-66", "Savio", 1000)

print(conta1.transfereValor(conta2, 500))
print()
conta1.gerar_extrato()
print()
conta2.gerar_extrato()
