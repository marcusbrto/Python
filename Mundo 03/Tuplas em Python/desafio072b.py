cont = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20: #Se num for maior ou igual a 0 E menor ou igual a 20
        break
    else:
        print("Tente novamente. ", end="") # end="" faz não pular linha (fica mais bonito no terminal)
print(f"Você digitou o número {cont[num]}!")