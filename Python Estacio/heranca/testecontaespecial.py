from Cliente import Cliente
from Conta import Conta
from ContaEspecial import ContaEspecial

cliente1 = Cliente("123", "Joao", 18,"Rua X")
cliente2 = Cliente("456", "Maria", 27,"Rua W")
cliente3 = Cliente("789", "Joana", 32, "Rua H")

#As três contas foram iniciadas, as contas comuns com saldo 2000 e a contaEspecial 1000
conta1 = Conta(cliente2, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 1000, 2000)

#impresso o saldo das três contas
print(f"Cliente: {cliente1.cpf} da conta comum {conta1.numero} possui saldo R$ {conta1.saldo}")
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R$ {conta2.saldo}")
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo R$ {conta3.saldo} e limite R$ {conta3.limite}\n")

#depositou 500 e tentou sacar 3000 da conta comum que não terá saldo
conta2.depositar(500)
#mensagem indicando saldo após depósito
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R$ {conta2.saldo} \n")

conta2.sacar(3000)
#mensagem indicando que não foi possível sacar e o saldo atual
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R$ {conta2.saldo} \n")

#depositou 100 e tentou sacar 2000 da conta especial que tem limite
conta3.depositar(100)
#mensagem indicando saldo após depósito
print(f"Cliente: {cliente3.cpf} da conta especal {conta3.numero} possui saldo R$ {conta3.saldo} e limite {conta3.limite}\n")

conta3.sacar(2000)
#mensagem indicando que foi possível sacar e saldo negativo
print(f"Cliente: {cliente3.cpf} da conta especal {conta3.numero} possui saldo R$ {conta3.saldo} e limite {conta3.limite}\n")

#tentativa de saque acima do limite
conta3.sacar(2000)
print(f"Cliente: {cliente3.cpf} da conta comum {conta3.numero} possui saldo R$ {conta3.saldo} e limite R$ {conta3.limite}\n")
