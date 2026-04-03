frase = "Olha só que, coisa interessante"
lista_cru = frase.split(",")

lista = []
for i, frase in enumerate(lista_cru):
    lista.append(lista_cru[i].strip())

print(lista)
print(lista_cru)   

frases_unidas = '-'.join(lista)
print(frases_unidas)