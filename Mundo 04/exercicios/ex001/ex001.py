#Declaracao de Classe
class Gafanhoto:
    def __init__(self): #metodo construtor
        #atributos de instancia:
        self.nome = ""
        self.idade = 0

    #Metodos de instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

#Declaracao de Classe, esses sao nossos objetos
g1 = Gafanhoto()
g1.nome = "Marcola"
g1.idade = 22
g1.aniversario()#soma mais um na idade
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Fodagames"
g2.idade = 49
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())