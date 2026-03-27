sexo = str(input("Digite seu sexo[F/M]: ")).strip().upper()[0]
while sexo not in "FfMm":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo[F/M]: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")