class Churrasco:
    def __init__(self,nome,qntpessoas):
        self.nome
        self.qntpessoas

    def analisar(self):
        print(f"Analisando {self.nome} com {self.qntpessoas} convidados")
        print(f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40")
        print(f"Recomendo comprar {self.qntpessoas * 0.4} de carne")
        print(f"O custo total será de {(self.qntpessoas * 0.4)*82.40}")
        print(f"Cada pessoa pagará {((self.qntpessoas * 0.4)*82.40)/self.qntpessoas} para participar.")

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()