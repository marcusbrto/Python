usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("Login autorizado")
else:
    print("Usuário ou senha inválidos")