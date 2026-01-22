palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO",
            "GRATIS","ESTUDAR","PRATICAR","TRABALHAR","MERCADO","PROGRAMADOR", "FUTURO")
for p in palavras: #para cada palavra na tupla
    print(f"\nNa palavra {p.upper()} temos: ",end="")
    for letra in p: #para cada letra em cada palavra
        if letra.lower() in "aeiou": #se tiver alguma dessas letras ele imprime
            print(letra, end=" ")