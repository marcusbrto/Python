import requests
import time

while True:
    try:
        resposta = requests.get("https://pudim.com.br/")#altere a url para a que voce quer
        print("Site Online")
    except:
        print("Site Offline")

    time.sleep(10)#tempo de busca em segundos
