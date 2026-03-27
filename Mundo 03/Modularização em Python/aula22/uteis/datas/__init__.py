# Funções relacionadas a datas

from datetime import datetime

def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

def hora_atual():
    return datetime.now().strftime("%H:%M:%S")

def data_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
