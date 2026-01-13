nome = str(input("Qual é seu nome? "))
if nome == "Marcola":
    print("Nome lindão :D")
elif nome == "Jesus"or nome == "Chaves"or nome == "Lucia":#"or" permite usar varias condições no mesmo elif
    print("Nome foda pae")
elif nome in "Skyrim":#o "in" funciona parecido com o "=="
    print("Melhor jogo de todos os tempos")
else:#o else é opcional
    print("Nome legal :)")
print("Tenha um bom dia!")