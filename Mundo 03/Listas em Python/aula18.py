"""teste = list()
teste.append("Marcola")
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 25
galera.append(teste[:])
print(galera)"""

"""galera = [["João",39],["Ana",89],["Marcola",22],["Maria",45]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")"""
galera = list()
dado = list()
totmaior = tormenor = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade")
        tormenor += 1
print(f"O total de pessoas maiores de idade é {totmaior} e menores é {tormenor}")