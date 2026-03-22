horario = input("Que horas são? (Ex: 18): ")

try:
    horas = int(horario.split(":")[0])

    if horas < 0 or horas > 23:
        print("Hora desconhecida")
    elif horas >= 18 and horas <= 23:
        print("Boa noite!")
    elif horas >= 12 and horas < 18:
        print("Boa tarde!")
    else:
        print("Bom dia!")

except:
    print("Não é um horário válido!")
