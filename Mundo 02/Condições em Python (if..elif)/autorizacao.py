perfil = input("Perfil do usuário: ")

if perfil == "admin":
    print("Acesso total")

elif perfil == "editor":
    print("Acesso parcial")

elif perfil == "leitor":
    print("Acesso normal")

else:
    print("Perfil inválido")