#Modul importieren
import math

#Rechenarten
class rechnen:
    def multi(self, input):
        return float(input[0]) * float(input[1])

    def potenz(self, input):
        return float(input[0]) ** float(input[1])

    def subtr(self, input):
        return float(input[0]) - float(input[1])*-

    def addit(self, input):
        return float(input[0]) + float(input[1])

    def divi(self, input):
        return float(input[0]) / float(input[1])
    
    def qwurzel(self, input):
        return math.sqrt(input)
    
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
            "_ q^dqw
            
            _" : rechner.qwurzel
}

