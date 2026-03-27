def escreva(texto):
    tamanho = len(texto) + 4
    linha = "~" * tamanho

    print(linha)
    print(f"  {texto}")
    print(linha)

escreva("Olá, Mundo!")
escreva("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec congue sapien, quis suscipit arcu.")
