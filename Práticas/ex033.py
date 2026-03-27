frase = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

i = 0
apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]
    qnt_aparicao_letra = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if apareceu_mais_vezes < qnt_aparicao_letra:
        apareceu_mais_vezes = qnt_aparicao_letra
        letra_que_mais_apareceu = letra_atual
    
    print(letra_atual)
    i += 1
    
print(f"A letra que mais apareceu foi '{letra_que_mais_apareceu}', {apareceu_mais_vezes} vezes.")