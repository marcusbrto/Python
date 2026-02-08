from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    elif idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


ano = int(input("Qual o ano de nascimento: "))
print(voto(ano))