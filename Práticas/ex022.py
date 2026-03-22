"""
Introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero = input("Vou dobrar o número que voce digitar: ")
try:
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float * 2:.2f}")
except:
    print("Isso não é um número")
