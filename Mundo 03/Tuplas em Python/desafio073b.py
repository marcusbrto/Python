times = ("Flamengo","Palmeiras","Cruzeiro Saf","Mirassol"
        ,"Fluminense","Botafogo","Bahia","São Paulo","Grêmio",
         "Red Bull Bragantino", "Atlético Mineiro Saf","Santo Fc",
         "Corinthias","Vasco da Gama Saf", "Vitória","Internacional",
         "Ceará","Fortaleza Ec Saf","Juventude","Sport Recife")
print("=" * 50)
print(f"Lista de times: {times}")#mostra todos
print("=" * 50)
print(f"Os 5 primeiros colocados {times[0:5]}")#os 5 primeiros
print("=" * 50)
print(f"Os 4 ultimos colocados {times[-4:-1]}")#os 4 ultimos
print("=" * 50)
print(f"Os times em ordem alfabética: {sorted(times)}")#ordem alfabetica
print("=" * 50)
print(f"O Fluminense está em {times.index("Fluminense")+1} posição.")#fazer uma busca dentro de
#uma tupla que retorna a posição, importante colocar +1 para ficar no numero humano
