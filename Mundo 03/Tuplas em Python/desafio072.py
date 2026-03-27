numextenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num = int(input("Digite um número entre 0 e 20: "))
while num < 0 or num > 20:
    num = int(input("\033[31mTente novamente\033. Digite um número entre 0 e 20: "))
print(f"Você digitou o número {numextenso[num]}!") #essa linha que transforma o numero em indice