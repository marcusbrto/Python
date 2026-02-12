from uteis import matematica
from uteis import texto
from uteis import cores
from uteis import datas
from uteis import verificacoes


texto.titulo("Teste do pacote utilidades")

print("Data atual:", datas.data_atual())

print("Dobro:", matematica.dobro(5))

print("Fatorial:", matematica.fatorial(5))

print(cores.colorir("Texto verde", cores.VERDE))

print("É par?", verificacoes.eh_par(10))
