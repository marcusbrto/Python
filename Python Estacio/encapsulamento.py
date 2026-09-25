class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero  # atributoprivado
        self.__saldo = saldo  # esse codigo gera erro pois saldo está privado, caso retire o __ ele volta a funcionar


def main():
    conta = Conta(1, 1000)
    saldo = conta.saldo
    # saldo = conta._Conta__saldo #desse jeito aqui nos burlamos o atributo privado e ele exibe


if __name__ == "__main__":
    main()
