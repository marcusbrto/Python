opcao = int(input("Por favor, selecione uma opção: "))

print("1 - Iniciar atendimento")
print("2 - Acompanhar meu pedido")
print("3 - Falar com atendente")

opcao = int(input("Sua escolha: "))

match opcao:
    case 1:
        print("Vamos iniciar seu atendimento")
    case 2:
        print("Vamos acompanhar seu atendimento")
    case 3:
        print("Vamos te encaminhar para um atendente")
    case _:
        print("Opção inválida")
