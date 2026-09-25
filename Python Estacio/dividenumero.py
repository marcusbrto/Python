import tkinter as tk
from tkinter import messagebox


def div_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"O quociente é : {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", " Divisão por zero não é permitida.")


# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de Divisão")

# Criando os widgets
label_num1 = tk.Label(janela, text="Dividendo:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Divisor:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_div = tk.Button(janela, text="Dividir", command=div_numeros)
botao_div.grid(row=2, columnspan=2, padx=100, pady=50)

# Rodando o loop principal
janela.mainloop()
