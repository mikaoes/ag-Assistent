# Module importieren
from tkinter import *
import core
import plugins

# Startwerte festlegen
eingabe=0
GroesseX=680
GroesseY=700
Red=(255,0,0)

# Funktionen definieren
def TextAnzeigen():
  print("Antwort(var):", response)
  ErgebnisA1.config(text=eingabe)
  ErgebnisA2.config(text=response)
def OkClick():
  global eingabe
  eingabe=eingabeF.get()
  print(eingabe)
  if eingabe=="":
    print("Bitte gib etwas ein!")
  else:
    global response
    response = core.request(eingabe) # Funktion aus Core gibt Antwort zurück
    TextAnzeigen()
    print("Else in OkClick ausgeführt")
    nichts2=StringVar()
    nichts2.set("")
    eingabeF.config(textvariable=nichts2)
    lastTextB.config(text=eingabe)
def xBClick():
  nichts=StringVar()
  nichts.set("")
  print("xB is clicked")
  eingabeF.config(textvariable=nichts)
def lastTextBClick(eingabe2):
  print("lastTextBClick aufgrufen")
  try:
    str(eingabe2)
    eingabe3=StringVar()
    eingabe3.set(eingabe2)
    print("xB is clicked")
    eingabeF.config(textvariable=eingabe3)
    eingabeF.config(textvariable = eingabe3)
    print("lastBClick beendet")
  except:
    print("Du kannst dies nicht tun, wenn du keinen Text eingegeben hast.")

# Tkinter vorbereiten
Fenster=Tk()
Fenster.configure(background="#FFDE00")
Fenster.minsize(GroesseX,GroesseY)
Fenster.title("Persönlicher Assistent")
Anzeige1=Label(Fenster, text="Hallo. Ich bin dein persönlicher Assistent",background="#FFDE00", foreground="black", font=('calibri', 13, 'bold'))
eingabeF=Entry(Fenster, width=35, background='#ADD8E6', foreground='black')
lastTextB=Button(Fenster, text="", width=35,command=lambda:lastTextBClick(eingabe))
lastTextB.place(x=100, y=100, height=40)
OkB=Button(Fenster, text="Ok", command=OkClick)
OkB.place(x=386, y=60, height=40, width=30)
xB=Button(Fenster, text="X", foreground="#000000", background='#ADD8E6', command=xBClick)
ErgebnisA1=Label(Fenster, text="")
ErgebnisA2=Label(Fenster, text="")
ErgebnisA2.place(x=50, y=440, height=220, width=600)
ErgebnisA1.place(x=50, y=200, height=220, width=600)
xB.place(x=345, y=65)
eingabeF.place(x=100, y=60, height=40)
Anzeige1.pack()
Fenster.mainloop()