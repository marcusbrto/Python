x = 1

def escopo():
    x = 3
    def outra_funcao():
        x = 12
        y = 1
        print(x,y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)