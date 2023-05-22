
try: 
    #import core
    pass
except ImportError:
    print("Fehler. Voakb import")
    quit()
# Daten auslesen
def auslesen():
    with open("plugins/VokabText.txt") as file:
        vokab=[]
        fileText=file.read()
        vokab.append(fileText.split(":"))
        for i in vokab:
            vokab.append(str(i).split(","))
        print(vokab)
def einspeichern(vokab):
    file=open("VokabText.txt")
    for a in file:
        a.append(",")
        for b in a:
            b.append(":")
    print(file)
    file.close()

auslesen()
einspeichern()
eingabe="Hallo"
#def translateMy(eingabe):
    #tranlator=ts.Translate(to_lang="zh")
    #return translator.translate(eingabe)

print("x")