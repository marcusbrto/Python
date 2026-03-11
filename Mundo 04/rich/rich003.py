from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome",justify="center",style="green",no_wrap=True)
tabela.add_column("Preço", justify="center",style="red",no_wrap=True)

tabela.add_row("Lapis","R$ 1,50")
tabela.add_row("Borracha","R$ 5,00")

print(tabela)

