#Entrada de dados para autenticacao
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

#autenticacao
if usuario == "admin" and senha == "123":
    #Só pergunta o perfil se o login for válido.

    perfil = input("Digite seu perfil (admin, editor, leitor): ")

    #autorizacao
    if perfil == "admin":
        print("Acesso total ao sistema")

    elif perfil == "editor":
        print("Acesso parcial ao sistema")

    elif perfil == "leitor":
        print("Somente leitura")

    else:
        print("Perfil inválido")

else:
    print("Usuário ou senha incorreto")