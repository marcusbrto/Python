num = int(input("Informe um número: "))

print("Análise do número {}:".format(num))
print("Unidade: {}".format(num % 10)) #divindo por 10 o resto da divisão sempre vai ser o outro digito
print("Dezena: {}".format((num // 10) % 10)) # o num // 10 remove a unidade e o % 10 pega o ultimo digito
print("Centena: {}".format((num // 100) % 10)) # num // 100 remove a unidade e a dezena, o % 10 pega o ultimo digito
print("Milhar: {}".format((num // 1000) % 10)) # num // 1000 remove a unidade, dezena e centena, o % 10 pega o ultimo digito
