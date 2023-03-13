# Module importieren
from tkinter import *

# Startwerte festlegen
GroesseX=800
GroesseY=600
Red=(255,0,0)

# Funktionen definieren
def OkClick():
    eingabe=eingabeF.get()
    print(eingabe)
def xBClick():
  pass
# Tkinter vorbereiten
Fenster=Tk()
Fenster.configure(background="#FFDE00")
Fenster.minsize(GroesseX,GroesseY)
Fenster.title("Persönlicher Assistent")
Anzeige1=Label(Fenster, text="Hallo. Ich bin dein persönlicher Assistent",background="#FFDE00", foreground="black", font=('calibri', 13, 'bold'))
eingabeF=Entry(Fenster, width=35, background='#ADD8E6', foreground='black')
OkB=Button(Fenster, text="Ok", command=OkClick())
OkB.place(x=135, y=40)
xB=Button(Fenster, text="X", foreground="#000000", background='#ADD8E6', command=xBClick())
xB.place(x=345, y=65)
eingabeF.place(x=100, y=60, height=40)
Anzeige1.pack()
Fenster.mainloop()
