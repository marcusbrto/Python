from ..interface import cabecalho

def arquivo_existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {arquivo} criado com sucesso!")


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arquivo, nome="desconhecido", idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um ERRO na adição dos dados no arquivo!")
        else:
            print(f"Novo cadastro de {nome} adicionado com sucesso!")