"""
Flag (Bandeira) - Marcar um local
None = Nao valor
is e is not = é ou nao é (tipo,valor,identidade)
id = identidade
"""

v1 = "a"
print(id(v1))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Nao faca algo")

print(passou_no_if, passou_no_if is None)
