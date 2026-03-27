def notas(*n, sit=False):
    """
    -> A Função para analisar notas de um aluno.
    :param n: Notas de um aluno(aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    total = len(n)
    soma = sum(n)
    maior = max(n)
    menor = min(n)

    media = soma / total

    if sit:
        if media >= 7:
            sit = 'BOM'
        elif media >= 5:
            sit = 'RAZOAVEL'
        else:
            sit = 'HORRIVEL'
    resp = {
        "total": total,
        "maior": maior,
        "menor": menor,
        "media": media,
        "sit": sit
    }
    return resp
#Programa Principal
resp = notas(5.5,9.5,10,6.5,sit=True)
print(resp)