sequencia = int(input("Quantos numeros da sequencia deseja mostrar: "))
num =  0
num2 = 1
c = 1
print(f"{num}\n{num2}")
while c <= sequencia:
    soma = num + num2 #faz a soma
    num = num2 # n1 passa a ter o valor de n2
    num2 = soma #n2 passa a ter a soma de n1 e n2
    #dessa forma fica a sequencia de fibonacci
    c = c + 1
    print(soma) #o que printa é a soma