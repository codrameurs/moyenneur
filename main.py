from tkinter import *
from moyenneur_module import *
'''
c'est le code
'''

class Fenetre():
    denom=False
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("Moyeneur")
        self.fenetre.geometry("700x550")
    def valider_note(self):
        note = entry.get()
        print(note)
        return note
    def valider_sur(self):
        sur=entry.get()
        phraseS.pack()
        print=(sur)
        return sur
    def menu_princ(self):
        note=0
        sur=0
        title=Label(fenetre,text="Bienvenue sur le moyeneur")
        title.place(x=300,y=0)
        entry=Entry(fenetre)
        entry.place(x=300,y=50)
        enter=Button(fenetre,text="entrer",command=valider_note)
        enter.place(x=300,y=100)
        phraseN=Label(fenetre,text="entrez votre note:")
        phraseN.place(x=300,y=30)
        phraseS=Label(fenetre,text="Sur combien est votre notre:")
        phraseS.place(x=300,y=30)
        enterS=Button(fenetre,text="entrer",command=valider_sur)
        enterS.place(x=300,y=100)
        texte = Label(fenetre,text="%d/%d"%(note,sur))
        texte.place(x=20,y=100)
        fenetre.mainloop()


fenetre=Fenetre()
