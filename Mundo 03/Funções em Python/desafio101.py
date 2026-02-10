
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    elif idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


ano = int(input("Qual o ano de nascimento: "))
print(voto(ano))