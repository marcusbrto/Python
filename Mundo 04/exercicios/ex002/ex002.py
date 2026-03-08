#Declaracao de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome,idade)
    """
    def __init__(self, nome = "", idade = 0): #metodo construtor
        #atributos de instancia:
        # cuidado para nao confundir, o self.nome é atributo e o nome nesse caso é o parametro que recebe o valor
        self.nome = nome
        self.idade = idade

    #Metodos de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self): #Dunder method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade} "

#Declaracao de Classe, esses sao nossos objetos
g1 = Gafanhoto("Marcola",22)
g1.aniversario()#soma mais um na idade
print(g1)
print(g1.__dict__)#atributo
print(g1.__getstate__())#metodo
print(g1.__class__)

print(g1.__doc__) #Dunder attribute, documente suas classes

g2 = Gafanhoto("Fodagames",49)
print(g2)

g3 = Gafanhoto()
print(g3)