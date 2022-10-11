from tkinter import *
import tkinter
from datetime import datetime

#CORES
cor1 = '#141a16' #PRETO
cor2 = '#f0f2f0' #BRANCO
cor3 = '#2cb851' #VERDE
cor4 = '#a82c19' #VERMELHO
cor5 = '#8d918d' #CINZA
cor6 = '#276ccc' #AZUL


#CRIAÇÃO DA JANELA
janela = Tk()
janela.title('Relogio Digital')
janela.geometry('440x180')
janela.resizable(width=FALSE, height=False)
janela.configure(bg=cor1)

def relogio():
    #VARIÁVEIS
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    data = tempo.strftime('%A %d/%B/%Y')

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=data)

l1 = Label(janela, text='', font=('Arial 80'), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(janela, text='', font=('Arial 20'), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)


relogio()
janela.mainloop()