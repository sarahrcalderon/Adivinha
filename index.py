import random
import tkinter as tk
from tkinter import messagebox

#Configuração do jogo
def verificarPalpite():
    try:
        palpite = int(entry_palpite.get())
        tentativasDeAdivinhacao(palpite)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

def tentativasDeAdivinhacao(palpite):
    global tentativas

    tentativas += 1
    dica = ""

    if palpite == numeroEscolhido:
        messagebox.showinfo("Parabéns!", f"Você acertou o número em {tentativas} tentativas.")
        reiniciar()
    elif palpite < numeroEscolhido:
        dica = "Humm, tente um número maior."
    else:
        dica = "Humm, tente um número menor."

    if palpite % 2 == 0:
        dica += " O número é PAR."
    else:
        dica += " O número é ÍMPAR."

    if palpite > numeroEscolhido:
        dica += f" O número que você escolheu é MAIOR que o número escolhido."
    elif palpite < numeroEscolhido:
        dica += f" O número que você escolheu é MENOR que o número escolhido."

    label_dica.config(text=dica)
    label_tentativas.config(text=f"Tentativas: {tentativas}")

def reiniciar():
    global numeroEscolhido, tentativas
    numeroEscolhido = random.randint(1, 100)
    tentativas = 0
    label_dica.config(text="")
    label_tentativas.config(text="Tentativas: 0")

def sairDoJogo():
    root.destroy()

# Inicio do jogo
numeroEscolhido = random.randint(1, 100)
tentativas = 0

root = tk.Tk()
root.title("Jogo de Adivinhação")
root.geometry("400x300")
root.iconphoto(True, tk.PhotoImage(file="icon.png"))  
root.config(bg="black")  # bk da janela como preto

label_instrucoes = tk.Label(root, text="Número entre 1 e 100. Tente adivinhar!", font=("Helvetica", 14), fg="white", bg="black")
label_instrucoes.pack(pady=10)

entry_palpite = tk.Entry(root, font=("Helvetica", 12))
entry_palpite.pack(pady=5)

#Botões
btn_verificar = tk.Button(root, text="Verificar Palpite", font=("Helvetica", 12), command=verificarPalpite)
btn_verificar.pack(pady=5)

label_dica = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="black")
label_dica.pack(pady=10)

label_tentativas = tk.Label(root, text="Tentativas: 0", font=("Helvetica", 12), fg="white", bg="black")
label_tentativas.pack(pady=10)

btn_reiniciar = tk.Button(root, text="Reiniciar Jogo", font=("Helvetica", 12), command=reiniciar)
btn_reiniciar.pack(pady=5)

btn_sair = tk.Button(root, text="Sair do Jogo", font=("Helvetica", 12), command=sairDoJogo)
btn_sair.pack(pady=5)

root.mainloop()
