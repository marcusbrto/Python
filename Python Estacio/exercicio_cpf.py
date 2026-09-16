def validar_cpf(cpf):
    #Remover caracteres não numericos
    cpf = "".join(filter(str.isdigit, cpf))
    
    #verifica se o cpf tem 11 digitos
    if len(cpf) != 11:
        return False
    
    #Verifica se todos os digitos são iguais(pode acontecer raramente)
    if cpf == cpf[0] * 11:
        return False
    
    #REGRAS DE CALCULO
    
    #Calculando o primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
        
    #Verificando o primeiro digito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False
    
    #Calculando o segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
        
    #Verificando o segundo digito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False
    
    #CPF válido
    return True
    
#testando a função
cpf = "123.456.789-09"
if validar_cpf(cpf):
    print(f"O CPF {cpf} é válido.")
else:
    print(f"O CPF {cpf} é inválido.")