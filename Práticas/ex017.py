primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(f"O {primeiro_valor=} é maior que {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"O {segundo_valor=} é maior que {primeiro_valor=}")
else:
    print(f"Os valores {segundo_valor=} e {primeiro_valor=} são IGUAIS")
    

