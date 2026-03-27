
class Churrasco:
    def __init__(self, nome, qntpessoas):
        self.nome = nome
        self.qntpessoas = qntpessoas

    def analisar(self):

        print(f"Analisando {self.nome} com {self.qntpessoas} convidados")
        print(f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40")
        print(f"Recomendo comprar {self.qntpessoas * 0.4} de carne")
        print(f"O custo total será de {(self.qntpessoas * 0.4) * 82.40:.2f}")
        print(f"Cada pessoa pagará {((self.qntpessoas * 0.4) * 82.40) / self.qntpessoas} para participar.")
c1 = Churrasco("Churras dos Amigos", 100)
c1.analisar()