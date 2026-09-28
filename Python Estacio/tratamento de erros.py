# Classe Calculadora com tratamento de exceções
class Calculadora:
    def adicao(self, x, y):
        try:
            return int(x + y)
        except TypeError:
            return "Erro: Tipos de dados inválidos para adição."
        except ValueError:
            return "Erro: Utilize Números"

    def subtracao(self, x, y):
        try:
            return int(x - y)
        except TypeError:
            return "Erro: Tipos de dados inválidos para subtração."
        except ValueError:
            return "Erro: Utilize Números"

    def multiplicacao(self, x, y):
        try:
            return int(x * y)
        except TypeError:
            return "Erro: Tipos de dados inválidos para multiplicação."
        except ValueError:
            return "Erro: Utilize Números"

    def divisao(self, x, y):
        try:
            return int(x / y)
        except TypeError:
            return "Erro: Tipos de dados inválidos para divisão."
        except ValueError:
            return "Erro: Utilize Números"
        except ZeroDivisionError:
            return "Não é possível dividir por zero"

# Testando as implementações
calculadora = Calculadora()

print(calculadora.adicao(5, 3))       # Saída: 8
print(calculadora.subtracao(5, 3))    # Saída: 2
print(calculadora.multiplicacao(5, "a"))# Saída: 15
print(calculadora.divisao(5, 0))    # Saída: Erro: Tipos de dados inválidos para divisão.
