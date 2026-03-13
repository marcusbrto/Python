from rich import print
from rich import inspect

class Funcionario:
    #Atributos de Classe
    empresa = "Curso em Video"

    def __init__(self, nome,setor,cargo):
        # Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

        #Metodos
    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.cargo} da empresa {Funcionario.empresa}"#atributo de classe tem que imprimir com a classe

#Declaracao de objetos
# Funcionario.empresa = "Hostnet"

c1 = Funcionario("Maria","Administracao","Diretora")
# inspect(c1, methods=True)
print(c1.apresentacao())

c2= Funcionario("Pedro","Setor TI","Programador")
print(c2.apresentacao())

inspect(c2)