import time
import os

minutos = int(input("Digite o tempo em minutos: "))

segundos = minutos * 60

print(f"Contando {minutos} minuto(s)...")
time.sleep(segundos)

print("Tempo acabou!")

# Barulho (funciona no Windows)
os.system("echo \a")
