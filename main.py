from tkinter import*
import pygame
from pygame import mixer

from PIL import Image, ImageTk
import os

#cores
co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#3fb5a3"
co3 = "#2e2d2c"
co4 = "#403d3d"
co5 = "#4a88e8"


#criando a janela
janela = Tk()
janela.title("")
janela.geometry("352x255")
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)


#Frames 

frame_esquerda = Frame(janela,width=150,height=150,bg=co3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky= NSEW)

frame_direita = Frame(janela,width=250,height=150,bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky= NSEW)

frame_baixo = Frame(janela,width=404,height=100,bg=co3)
frame_baixo.grid(row=1, column=0,columnspan=3, pady=1, padx=0, sticky= NSEW)



#confgurando frame esquerda
img_1 = Image.open('icon1.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130,image=img_1, compound=LEFT,padx=10,anchor='nw',font=('Ivy 16 bold'),bg=co3,fg=co3)
l_logo.place(x=8, y= 10)


#criando funcoes
def stop_musica():
    mixer.music.stop()

def play_musica():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()
    print(rodando)

def pausar_musica():
    mixer.music.pause()

def continuar_musica():
    mixer.music.unpause()

def proxima_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index+1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

def anterior_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index-1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando




#configurando frame direita

lista = ['João','Luiz', 'Alexandre','João','Luiz', 'Alexandre','João','Luiz', 'Alexandre','João','Luiz', 'Alexandre']


listbox = Listbox(frame_direita,selectmode=SINGLE,width=22,height=10,font=('arial 9 bold'),bg=co3,fg=co1)
listbox.grid(row=0,column=0)

s = Scrollbar(frame_direita)
s.grid(row=0,column=1,sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


#configurando frame baixo
l_rodando = Label(frame_baixo,text='Escolha uma Musica', width=44,justify=LEFT,anchor='nw',font=('Ivy 10'),bg=co1,fg=co4)
l_rodando.place(x=0, y= 1)



img_2 = Image.open('2.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)


b_anterior = Button(frame_baixo, width=40,command=anterior_musica,height=40,image=img_2,font=('Ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=co3,fg=co4)
b_anterior.place(x=38, y= 35)


#botão 3
img_3 = Image.open('3.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)


b_play = Button(frame_baixo, width=40,command=play_musica,height=40,image=img_3,font=('Ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=co3,fg=co4)
b_play.place(x=84, y= 35)

#botão 4
img_4 = Image.open('4.png')
img_4.rotate(45)
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)


b_proximo = Button(frame_baixo, width=40,command=proxima_musica,height=40,image=img_4,font=('Ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=co3,fg=co4)
b_proximo.place(x=130, y= 35)

#botão 5
img_5 = Image.open('5.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)


b_pausar = Button(frame_baixo, width=40,command=pausar_musica,height=40,image=img_5,font=('Ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=co3,fg=co4)
b_pausar.place(x=176, y= 35)

#botão 6
img_6 = Image.open('6.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)


b_continuar = Button(frame_baixo, width=40,command=continuar_musica,height=40,image=img_6,font=('Ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=co3,fg=co4)
b_continuar.place(x=222, y= 35)

#botão 7
img_7 = Image.open('7.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)


b_stop = Button(frame_baixo, width=40,command=stop_musica,height=40,image=img_7,font=('Ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=co3,fg=co4)
b_stop.place(x=268, y= 35)

os.chdir(r'C:\Users\DroidLator\OneDrive\Área de Trabalho\musicas')
musicas = os.listdir()

def mostrar():
    for item in musicas:
        listbox.insert(END,item)

mostrar()




mixer.init()
janela.mainloop()