times = ("Flamengo","Palmeiras","Cruzeiro Saf","Mirassol","Fluminense","Botafogo","Bahia","São Paulo","Grêmio",
         "Red Bull Bragantino", "Atlético Mineiro Saf","Santo Fc","Corinthias","Vasco da Gama Saf", "Vitória",
         "Internacional","Ceará","Fortaleza Ec Saf","Juventude","Sport Recife")

print("\033[32mOs cinco primeiros colocados são:\033[m")
for c in range(0,5):
    print(times[c])

print("\033[32mOs cinco ultimos são:\033[m")
for c in range(-5,-0):
    print(times[c])

print("\033[32mOs times em ordem alfabetica:\033[m")
print(sorted(times))

print("A posição do Santos é:")
print(times.index("Santo Fc") + 1) # o +1 é porque a contagem começa do ZERO então na linguagem humana ele é o 12
