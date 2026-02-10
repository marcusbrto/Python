def notas(*n, sit=False):
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
resp = notas(5.5,2.5,1.5,sit=True)
print(resp)