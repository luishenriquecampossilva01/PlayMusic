from tkinter import*

from PIL import Image, ImageTk

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


#configurando frame direita

lista = ['João','Luiz', 'Alexandre','João','Luiz', 'Alexandre','João','Luiz', 'Alexandre','João','Luiz', 'Alexandre']


listbox = Listbox(frame_direita,selectmode=SINGLE,width=22,height=10,font=('arial 9 bold'),bg=co3,fg=co1)
listbox.grid(row=0,column=0)

s = Scrollbar(frame_direita)
s.grid(row=0,column=1,sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)
for item in lista:
    listbox.insert(END,item)

janela.mainloop()