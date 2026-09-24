import tkinter as tk


def atualizar_coordenadas(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f"Coordenadas do mouse: X={x}, Y={y}"


# Criando a janela
janela = tk.Tk()
janela.title("Tratamento de Eventos - Coordenadas do Mouse")

# Criando o widget de rótulo
label_coordenadas = tk.Label(
    janela, text="Mova o mouse sobre a janela para ver as coordenadas"
)
label_coordenadas.pack(padx=200, pady=100)

# Ligando o evento de movimento do mouse à função
janela.bind("<Motion>", atualizar_coordenadas)

# Rodando o loop principal
janela.mainloop()
