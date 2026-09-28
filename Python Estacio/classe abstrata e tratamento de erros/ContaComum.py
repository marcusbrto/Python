from ClasseAbstrata import *

class ContaComum(ContaCliente):
    def calculo_rendimento(self):
        # Implementação fictícia para cálculo de rendimento
        return self.valor_investido * self.taxa_rendimento - (self.IOF + self.IR)

# Instanciando a subclasse concreta
cc1 = ContaComum(1, 0.1, 0.25, 1000, 0.1)
print(cc1.calculo_rendimento())