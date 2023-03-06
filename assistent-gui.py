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

# Tkinter vorbereiten
Fenster=Tk()
Fenster.configure(background="#FFDE00")
Fenster.minsize(GroesseX,GroesseY)
Fenster.title("Persönlicher Assistent")
Anzeige1=Label(Fenster, text="Hallo. Ich bin dein persönlicher Assistent",background="#FFDE00", foreground="black", font=('calibri', 13, 'bold'))
eingabeF=Entry(Fenster, width=25, background='blue', foreground='black')
OkB=Button(Fenster, text="Ok", command=OkClick())
eingabeF.place(x=100, y=60, height=30)
Anzeige1.pack()
Fenster.mainloop()