palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO",
            "GRATIS","ESTUDAR","PRATICAR","TRABALHAR","MERCADO","PROGRAMADOR", "FUTURO")
for pos in range (0,len(palavras)):
    print(f"Na palavra {palavras[pos]} temos ",end="")
    for letra in palavras[pos]:
            if letra.upper() in "AEIOU":
                print(letra.upper(),end="")
    print()