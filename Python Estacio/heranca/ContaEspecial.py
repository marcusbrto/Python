from Conta import Conta
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor: #na conta especial a gente verifica o saldo e limite e na conta normal somente o saldo
            print(f"Não existe saldo suficiente conta numero {self.numero} cliente {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True