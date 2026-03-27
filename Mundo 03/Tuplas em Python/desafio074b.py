from random import randint
c = 0
num = randint(1, 20),randint(1, 20),randint(1, 20),randint(1, 20),randint(1, 20)
print(f"Eu sorteei os números: ", end="")
for c in range(0,5):
    print(f"{num[c]}", end=" ")

print(f"\nO maior valor sorteado foi {max(num)}.")
print(f"O menor valor sorteado foi {min(num)}.")
