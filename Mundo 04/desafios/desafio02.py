from rich import print
from rich.table import Table


class Produto:
    def __init__(self, nome="", valor=0):
        self.valor = valor
        self.nome = nome

    def etiqueta(self):
        tabela = Table(title="Produto")

        tabela.add_column("Nome", justify="center", style="green")
        tabela.add_column("Valor", justify="center", style="green")

        tabela.add_row(self.nome, f"R$ {self.valor}")

        print(tabela)


p1 = Produto("Iphone 17 Pro Max", 25000.85)
p1.etiqueta()