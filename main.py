from tkinter import *

def init():
    fenetre = Tk()
    fenetre.title("Moyeneur")
    fenetre.geometry("700x550")
    return fenetre
def valider():
    print(entry.get())
    texte = Label(fenetre,text=entry.get())
    texte.place(x=20,y=100)

fenetre = init()

title=Label(fenetre,text="Bienvenue sur le moyeneur")
title.place(x=300,y=0)
enter=Button(fenetre,text="entrer",command=valider)
enter.place(x=300,y=100)
entry=Entry(fenetre)
entry.place(x=300,y=50)
fenetre.mainloop()