nome = "Marcus Vinicius"

contador = 0
novo_nome = ""

while contador < len(nome):
    letra = nome[contador]
    novo_nome += f"*{letra}"
    contador += 1
    
print(novo_nome)
    
    