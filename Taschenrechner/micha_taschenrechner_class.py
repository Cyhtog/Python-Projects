# Taschenrechner mit Klassen von Michael Ahmels

# Klassen Definieren
class Main:
    def zweiWerteVerrechnen(self):
        abbruch = False
        mitAltemErgebnisWeiterRechnen = False
        while abbruch == False:
            rechenart = "Fehler"
            while rechenart == "Fehler":
                rechenart = Erfragen.rechenart(self)
            if rechenart == "Addition":
                if mitAltemErgebnisWeiterRechnen == True:
                    a = ergebnis
                else:
                    a = Erfragen.zahlAdditionA(self)
                b = Erfragen.zahlAdditionB(self)
                ergebnis = Berechnung.addition(self, a, b)

            elif rechenart == "Subtration":
                if mitAltemErgebnisWeiterRechnen == True:
                    a = ergebnis
                else:
                    a = Erfragen.zahlSubtraktionA(self)
                b = Erfragen.zahlSubtraktionB(self)
                ergebnis = Berechnung.subtraktion(self, a, b)

            elif rechenart == "Multiplikation":
                if mitAltemErgebnisWeiterRechnen == True:
                    a = ergebnis
                else:
                    a = Erfragen.zahlMultiplikationA(self)
                b = Erfragen.zahlMultiplikationB(self)
                ergebnis = Berechnung.multiplikation(self, a, b)

            elif rechenart == "Division":
                if mitAltemErgebnisWeiterRechnen == True:
                    a = ergebnis
                else:
                    a = Erfragen.zahlDivisionA(self)
                b = Erfragen.zahlDivisionB(self)
                ergebnis = Berechnung.division(self, a, b)

            Ausgabe.ergebnis(ergebnis, rechenart)
            abbruch, mitAltemErgebnisWeiterRechnen = Erfragen.weiterRechnen(ergebnis)
class Erfragen:
    def rechenart(self):
        rechenart = input(
            "Bitte geben Sie a für Addition, s für Subtration, m für Multiplikation und d für Division ein:\n")
        if rechenart == "a":
            return "Addition"
        elif rechenart == "s":
            return "Subtration"
        elif rechenart == "m":
            return "Multiplikation"
        elif rechenart == "d":
            return "Division"
        else:
            print("Sie haben eine falsche Eingabe gemacht!")
            return "Fehler"

    def zahlAdditionA(self):
        a = None
        while a == None:
            a = input("Bitte geben Sie den ersten Summanden ein:\n")
            a = Erfragen.zahlUmwandeln(a)
        return a

    def zahlAdditionB(self):
        b = None
        while b == None:
            b = input("Bitte geben Sie den zweiten Summanden ein:\n")
            b = Erfragen.zahlUmwandeln(b)
        return b

    def zahlSubtraktionA(self):
        a = None
        while a == None:
            a = input("Bitte geben Sie den Minuenden ein:\n")
            a = Erfragen.zahlUmwandeln(a)
        return a

    def zahlSubtraktionB(self):
        b = None
        while b == None:
            b = input("Bitte geben Sie den Subtrahenden ein:\n")
            b = Erfragen.zahlUmwandeln(b)
        return b

    def zahlMultiplikationA(self):
        a = None
        while a == None:
            a = input("Bitte geben Sie den Multipliplikand ein:\n")
            a = Erfragen.zahlUmwandeln(a)
        return a

    def zahlMultiplikationB(self):
        b = None
        while b == None:
            b = input("Bitte geben Sie den Multiplikator ein:\n")
            b = Erfragen.zahlUmwandeln(b)
        return b

    def zahlDivisionA(self):
        a = None
        while a == None:
            a = input("Bitte geben Sie den Dividenden ein:\n")
            a = Erfragen.zahlUmwandeln(a)
        return a

    def zahlDivisionB(self):
        b = None
        while b == None or b == 0:
            b = input("Bitte geben Sie den Divisor ein:\n")
            b = Erfragen.zahlUmwandeln(b)
            if b == 0:
                print("Division durch 0 ist nicht definiert!")
        return b

    # Umwandlung in einen Float

    def zahlUmwandeln(x):
        try:
            x = x.replace(",",".")
            x = float(x)
            return x
        except:
            print("Sie haben keine Zahl eingegeben!")

    def weiterRechnen(self):
        abfrage = "j"
        while abfrage != "n" or "j" or "w":
            abfrage = input(
                "Wollen sie noch eine Berechnung durchführen? j für Ja, n für Nein und w für mit altem Wert weiter rechnen:\n")
            if abfrage == "n":
                abbruch = True
                mitAltemErgebnisWeiterRechnen = False
                break
            elif abfrage == "j":
                abbruch = False
                mitAltemErgebnisWeiterRechnen = False
                break
            elif abfrage == "w":
                abbruch = False
                mitAltemErgebnisWeiterRechnen = True
                break
            else:
                print("Sie haben sich vertippt!")
        return abbruch, mitAltemErgebnisWeiterRechnen

class Berechnung:
    # Konstruktormethode
    def __init__(self, rechenart = "(leer)"):
        pass
    def addition(self, a, b):
        return a + b
    def subtraktion(self, a, b):
        return a - b
    def multiplikation(self, a, b):
        return a * b
    def division(self, a, b):
        return a / b

class Ausgabe:
    # Ausgabe des Ergebnises

    def ergebnis(ergebnis, rechenart):

        ergebnisStr = str(ergebnis)
        ergebnisStr = ergebnisStr.replace(".", ",")
        ergebnisStrPartitioniert = ergebnisStr.partition(",")
        ergebnisListLinks = list(ergebnisStrPartitioniert[0])
        ergebnisListLinks.reverse()
        drehen = "j"
        ergebnisStrLinks = Ausgabe.tausenderPunkt(ergebnisListLinks, drehen)

        ergenisListRechts = list(ergebnisStrPartitioniert[2])
        drehen = "n"
        ergebnisStrRechts = Ausgabe.tausenderPunkt(ergenisListRechts, drehen)
        try:
            ergebnisIntRechts = int(ergebnisStrRechts)
        except:
            print("kein Int")
            ergebnisIntRechts = 1

        if ergebnisIntRechts == 0:
            ergebnisStr = ergebnisStrLinks
        else:
            ergebnisStr = ergebnisStrLinks + ergebnisStrPartitioniert[1] + ergebnisStrRechts
        print("Die", rechenart, "ergab das Ergebnis:\n", ergebnisStr)

    # Hinzufügen des 1000er Punktes

    def tausenderPunkt(ergebnisList, drehen):
        charakterZähler = 0
        ergebnisStr = ""
        for i in ergebnisList:
            if charakterZähler == 3:
                ergebnisStr = ergebnisStr + "." + i
                charakterZähler = 1
            else:
                ergebnisStr = ergebnisStr + i
                charakterZähler = charakterZähler + 1

        if drehen == "j":
            ergebnisList = list(ergebnisStr)
            ergebnisList.reverse()
            ergebnisStr = ""
            for i in ergebnisList:
                ergebnisStr = ergebnisStr + i
        return ergebnisStr


# Klassen erstellen und aufrufen

Programm = Main()
Programm.zweiWerteVerrechnen()
print("Danke, noch einen schönen Tag!")