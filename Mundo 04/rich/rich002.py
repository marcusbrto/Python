from django.template.defaultfilters import length
from rich import print
from rich.panel import Panel

caixa = Panel("Painel teste lib rich",title="Mensagem", style="red")

print(caixa)