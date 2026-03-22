# (caractere)(><)^(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# sinal - + ou -
# ex.: 0>-1000,.1f
# conversion flags - !r !s !a

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^10}")
print(f"{1000.480932890321:0=+10,.1f}")
