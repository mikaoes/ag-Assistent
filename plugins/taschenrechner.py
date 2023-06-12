#Modul importieren
import math

#Rechenarten
class rechnen:
    def multi(self, input):
        return float(input[0]) * float(input[1])

    def potenz(self, input):
        return float(input[0]) ** float(input[1])

    def subtr(self, input):
        return float(input[0]) - float(input[1])

    def addit(self, input):
        return float(input[0]) + float(input[1])

    def divi(self, input):
        return float(input[0]) / float(input[1])
    
    def qwurzel(self, input):
        return math.sqrt(float(input[0]))

    def fakult(self, input):
        ergebnis = 1
        for i in range(1, int(input[0])+1):
            ergebnis = ergebnis * i
        return ergebnis
    
rechner = rechnen()

#commands
commands = {
            "Rechne _ mal _" : rechner.multi,
            "Was ist _ mal _" : rechner.multi,
            "_ mal _" : rechner.multi,
            "Multipliziere _ und _" : rechner.multi,
            "Rechne _ hoch _" : rechner.potenz,
            "Die _ rechner.Potenz von _" : rechner.potenz,
            "Was ist _ hoch _" : rechner.potenz,
            "_ hoch _" : rechner.potenz,
            "Rechne _ minus _" : rechner.subtr,
            "Was ist _ minus _" : rechner.subtr,
            "_ minus _" : rechner.subtr,
            "Subtrahiere _ und _" : rechner.subtr,
            "Ziehe Quadratwurzel von _" : rechner.qwurzel,
            "Ziehe Wurzel aus _" : rechner.qwurzel,
            "Mache Wurzel aus _" : rechner.qwurzel,
            "Ziehe die Quadratwurzel aus _." : rechner.qwurzel,
            "Was ist die Wurzel von _" : rechner.qwurzel,
            "Was ist die Wurzel von _?" : rechner.qwurzel,
            "Was ist die Quadratwurzel von _" : rechner.qwurzel,
            "Was ist die Quadratwurzel von _?" : rechner.qwurzel,
            "Berechne Fakultät von _" : rechner.fakult,
            "Berechne die Fakultät von _." : rechner.fakult,
            "Was ist die Fakultät von _" : rechner.fakult,
            "Was ist die Fakultät von _?" : rechner.fakult,
            "Dividiere _ und _" : rechner.divi,
            "_ geteilt durch _" : rechner.divi,
            " Was ist _ geteilt durch _" : rechner.divi
}

