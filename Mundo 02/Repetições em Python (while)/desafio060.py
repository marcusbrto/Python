num = int(input("Digite um número para mostrar seu fatorial: "))

fatorial = c = 1 # variavel fatorial guarda o resultado
# C é contador
#começa com 1 porque é um elemento neutro na multiplicação e fatorial nunca multiplica com 0

while c <= num:#quando c chegar no valor de num ele para o ciclo
    fatorial = fatorial * c # ele começa com 1 * 1, fatorial guarda o resultado e depois c ganha +1, depois vira 1*2, depois 2*3 e por ai vai
    c += 1

print(f"\nO fatorial do número {num} é {fatorial}")
