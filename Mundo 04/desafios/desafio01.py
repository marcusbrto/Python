from rich import print

class Funcionario:
    """
    Função simples que faz a apresentação com o nome, cargo e setor.
    """

    def __init__(self,nome="",cargo="",setor=""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Video"


c1 = Funcionario("Marcola","TI","Programador")
print(c1.apresentacao())

c2 = Funcionario("Pedro","Diretor","Senior")
print(c2.apresentacao())