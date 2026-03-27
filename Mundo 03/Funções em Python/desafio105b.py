def notas(*n, sit=False):
    """
    -> Função para analisar notas de um aluno.
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a função
    :return: retorna um dicionario com as informações
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = "BOA"
        elif r['media'] >= 5:
            r['situacao'] = "RAZOAVEL"
        else:
            r['situacao'] = "RUIM"

    return r

#Programa Principal
resp = notas(2.5,3.5,sit=True)
print(resp)