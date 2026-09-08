def calcular_expressao():
    expressao = input("Digite uma expressão matemática: ")
    
    try: #TENTE EXECUTAR ESSE
        resultado = eval(expressao)
        print(f"O resultado da expressão é {expressao}")
    except Exception as e: #SE DER ERRO RETORNE ISSO
        print(f"Erro ao avaliar a expressão: {e}")
        
calcular_expressao()